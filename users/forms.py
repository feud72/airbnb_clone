from django import forms
from . import models


class LoginForm(forms.ModelForm):
    """LoginForm definition."""

    class Meta:
        model = models.User
        fields = ["email", "password"]
        widgets = {"password": forms.PasswordInput}

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    """SignUpForm definition."""

    class Meta:
        model = models.User
        fields = ["email", "first_name", "last_name"]

    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_password1(self):
        password = self.cleaned_data["password"]
        password1 = self.cleaned_data["password1"]
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        username = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.username = username
        user.set_password(password)
        user.save()
