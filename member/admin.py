from django.contrib import admin

from member.models import IdDefaultInfo, UserInfo


# Register your models here.
class AdminIdDefaultInfo(admin.ModelAdmin):
    list_display = ["user_id", "user_passwd", "user_email"]


class AdminUserInfo(admin.ModelAdmin):
    list_display = ["user_favorite"]


admin.site.register(IdDefaultInfo, AdminIdDefaultInfo)
admin.site.register(UserInfo, AdminUserInfo)
