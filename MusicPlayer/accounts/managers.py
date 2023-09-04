from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, name, password, **other_fields):
        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have a name")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password, **other_fields):
        user = self.create_user(
            username=username, email=email, name=name, password=password, **other_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
