from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from .models import Artist, Listener


class AuthBackend(BaseBackend):
    def authenticate(self, request, is_artist=False, username=None, password=None):
        if username is None or password is None:
            return None
        if is_artist:
            UserModel = Artist
        else:
            UserModel = Listener
        try:
            if "@" in username:
                user = UserModel.objects.get(email=username)
            else:
                user = UserModel.objects.get(username=username)

        except:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return Listener.objects.get(pk=user_id)
        except Listener.DoesNotExist:
            try:
                return Artist.objects.get(pk=user_id)
            except Artist.DoesNotExist:
                return None
