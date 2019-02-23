from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    # TODO: Define form fields here

    class Meta:
        model = User
        fields = ['email','password']

        widget = {
            'password': forms.PasswordInput(attrs = {'id': 'client_password','type': 'password'},render_value = False),
            'email': forms.EmailInput(attrs = {'id': 'client_email', 'placeholder':'Please enter your email address'})
        }
