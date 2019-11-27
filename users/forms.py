from django import forms
from . import models


class LoginForm(forms.Form):
    """LoginForm definition."""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")
        return email

    def clean_password(self):
        print("clean ps")