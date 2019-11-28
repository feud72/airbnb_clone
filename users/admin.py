from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom Uesr Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom  Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "bio",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "is_superuser",
        "superhost",
        "email_verified",
        "email_secret"
    )
    list_filter = UserAdmin.list_filter
