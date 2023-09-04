from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class BaseUser(AbstractBaseUser, PermissionsMixin):
    class Gender(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        OTHER = "Other"

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="users", null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length=6, choices=Gender.choices, null=True, blank=True
    )
    birthday = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "name"]

    def __str__(self):
        return self.username


# Create your models here.
