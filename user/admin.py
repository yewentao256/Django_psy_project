from django.contrib import admin
from .models import User, Consultant


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("注册信息", {"fields": ["create_time", "username"]}),
        ("用户信息", {"fields": ["name", "user_nickname", "sex", "birthday", "user_email", "signature", "avatar", "mobile",
                             "idcard", "user_status", "address"]}),
    ]
    list_display = ("id", "username", "user_nickname", "mobile")
    list_filter = ("mobile", "username")  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    ordering = ["id", "username", "user_nickname"]  # 这样设置，publish是除id外的第一键


class ConsultantAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "qq")
    list_filter = ("qq",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    ordering = ["id", "user"]  # 这样设置，publish是除id外的第一键


admin.site.register(User, UserAdmin)
admin.site.register(Consultant, ConsultantAdmin)
