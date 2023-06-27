from django.contrib import admin

from board.models import Content


# Register your models here.
class AdminContent(admin.ModelAdmin):
    list_display = ["user_id", "content_subject", "content_article"]


admin.site.register(Content, AdminContent)
