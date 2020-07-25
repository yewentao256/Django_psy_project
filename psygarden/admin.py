from django.contrib import admin
from .models import Message,Comment

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "create_time", "type")
    list_filter = ("create_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    date_hierarchy = "create_time"  # 一个可以选择任意日期的过滤器
    ordering = ["id", "create_time"]  # 这样设置，publish是除id外的第一键

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "message", "create_time")
    list_filter = ("create_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    date_hierarchy = "create_time"  # 一个可以选择任意日期的过滤器
    ordering = ["id", "create_time"]  # 这样设置，publish是除id外的第一键

admin.site.register(Message, MessageAdmin)
admin.site.register(Comment, CommentAdmin)