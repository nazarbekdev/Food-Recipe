from django.contrib import admin

from accounts.models.user_follow import UserFollow
from accounts.models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name')


@admin.register(UserFollow)
class UserFollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user')
