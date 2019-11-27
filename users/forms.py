from django import forms


class LoginForm(forms.Form):
    """LoginForm definition."""

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    