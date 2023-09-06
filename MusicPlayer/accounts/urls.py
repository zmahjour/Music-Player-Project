from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("register/", views.UserRegisterView.as_view(), name="user_register"),
    path("logout/", views.UserLogoutView.as_view(), name="user_logout"),
]
