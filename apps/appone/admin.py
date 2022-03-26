from typing import Optional

from django.contrib import admin
from django.http import HttpRequest
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    User
)

class CustomUserAdmin(UserAdmin):
    readonly_fields: tuple = ()
    def get_readonly_fields(self, request: HttpRequest,
                            obj: Optional[User] = None) -> tuple:
        if obj:
            return self.readonly_fields + (
                'username','surname',
                'email','is_active',
                'is_staff','is_superuser',
                'date_joined','last_login')
        return self.readonly_fields


class UserAdmin(admin.ModelAdmin):
    
    MAX_USER_EDITABLE_AGE = 18
    readonly_fields: tuple = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
        )
    list_filter = (
        'username',
        'surname',
    )
    search_fields = (
        'email',
    )
    list_display = (
        'name',
        'surname',
    )
    USER_MAX_AGE = 30
    
    def user_age_validation(
        self,
        obj: Optional[User]
    ) -> tuple:
        if obj and obj.age <= self.USER_MAX_AGE:
            return True
        return False

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[User] = None
    ) -> tuple:

        result: bool = self.user_age_validation(obj)
        if result:
            return self.readonly_fields + ('birthday',)
        return self.readonly_fields

