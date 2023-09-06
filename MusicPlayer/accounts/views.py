from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import LoginForm, ListenerCreationForm


class UserLoginView(View):
    form_class = LoginForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            is_artist = cd["is_artist"]
            username = cd["username"]
            password = cd["password"]
            user = authenticate(
                request, is_artist=is_artist, username=username, password=password
            )
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in", "success")
                return redirect("songs:home")
            messages.error(request, "The username or password was incorrect", "danger")
        return redirect("songs:home")


class UserRegisterView(View):
    form_class = ListenerCreationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "You have successfully registered", "success")

            send_mail(
                subject="Welcome to Music Player",
                message="Enjoy Listening!",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                html_message=render_to_string(
                    "accounts/welcome_email.html", context={"name": user.name}
                ),
            )
            messages.info(request, "Check your email", "info")

            return redirect("songs:home")
        messages.warning(request, "Something was wrong; try again", "warning")
        return redirect("songs:home")


class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect("songs:home")
