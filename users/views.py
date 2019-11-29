import os
import requests
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from . import forms, models


class LoginView(FormView):
    """LoginView definition."""

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")
    initial = {"email": "feud72@gmail.com"}

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(LogoutView):
    """LogoutView definition."""

    next_page = reverse_lazy("core:home")


class SignUpView(FormView):
    """SignUpView definition."""

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        'first_name': "Nicolas",
        'last_name': "Serr",
        "email": "itn@las.com",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):

    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.save()
        # to do: add success message
    except models.User.DoesNotExist:
        # to do: add error message
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GH_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user")


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GH_ID")
        client_secret = os.environ.get("GH_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            res = requests.post(f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                                headers={"Accept": "application/json"}
                                )
            res_json = res.json()
            error = res_json.get("error", None)
            if error:
                raise GithubException()
            else:
                access_token = res_json.get("access_token")
                profile_res = requests.get("https://api.github.com/user",
                                           headers={"Authorization": f"token {access_token}",
                                                    "Accept": "application/json"})
                profile_json = profile_res.json()
                username = profile_json.get("login", None)
                if username:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    if models.User.objects.filter(email=email).exists():
                        user = models.User.objects.get(username=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException()
                    else:
                        user = models.User.objects.create(
                            username=email, first_name=name, bio=bio, email=email, login_method=models.User.LOGIN_GITHUB)
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException()
    except GithubException:
        # send error message
        return redirect(reverse("core:home"))
