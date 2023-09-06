from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Listener, Artist, BaseUser, Band


@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    list_display = ["username", "email", "is_staff"]
    list_filter = ["is_staff", "country", "gender"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal info",
            {
                "fields": [
                    "name",
                    "bio",
                    "image",
                    "country",
                    "city",
                    "gender",
                    "birthday",
                ]
            },
        ),
        ("Permissions", {"fields": ["is_active", "is_staff"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "fields": ["username", "email", "name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["username", "email"]
    ordering = ["username"]
    filter_horizontal = []


@admin.register(Listener)
class ListenerAdmin(BaseUserAdmin):
    list_filter = ["is_staff", "country", "gender", "account_type"]
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal info",
            {
                "fields": [
                    "name",
                    "bio",
                    "image",
                    "country",
                    "city",
                    "gender",
                    "birthday",
                ]
            },
        ),
        ("Permissions", {"fields": ["account_type", "is_active", "is_staff"]}),
    ]


@admin.register(Artist)
class ArtistAdmin(BaseUserAdmin):
    fieldsets = [
        (None, {"fields": ["username", "email", "password"]}),
        (
            "Personal info",
            {
                "fields": [
                    "name",
                    "bio",
                    "image",
                    "country",
                    "city",
                    "gender",
                    "birthday",
                    "band",
                ]
            },
        ),
        ("Permissions", {"fields": ["is_active", "is_staff"]}),
    ]


admin.site.register(Band)
