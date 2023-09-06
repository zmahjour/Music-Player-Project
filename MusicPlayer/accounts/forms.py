from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import BaseUser, Listener, Artist


class ListenerCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Listener
        fields = ["username", "email", "name"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter Your Name",
                    "class": "form-control",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Enter Your Username",
                    "class": "form-control",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Enter Your Email",
                    "class": "form-control",
                }
            ),
        }


class LoginForm(forms.Form):
    is_artist = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"id": "is_artist", "name": "is_artist"}),
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "placeholder": "Enter Your Email or Username",
                "class": "form-control",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "placeholder": "Enter Password",
                "class": "form-control",
            }
        )
    )


class ListenerChangeForm(UserChangeForm):
    class Meta:
        model = Listener
        fields = "__all__"


class ArtistChangeForm(UserChangeForm):
    class Meta:
        model = Artist
        fields = "__all__"
