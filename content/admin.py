from django.contrib import admin
from .models import Consultant, Lecture, Resource, Articles, PsyTest


class ConsultantAdmin(admin.ModelAdmin):
    list_display = ("name", "telephone", "QQ")
    list_filter = ("register_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示
    search_fields = ("name", "telephone")
    date_hierarchy = "register_time"  # 一个可以选择任意日期的过滤器
    ordering = ["name", "register_time"]  # 这样设置，publish是除id外的第一键


class LectureAdmin(admin.ModelAdmin):
    list_display = ("name", "time")
    list_filter = ("time",)  # time增加一个过滤器，可以根据日期选择显示
    search_fields = ("name", "time")
    date_hierarchy = "time"  # 一个可以选择任意日期的过滤器
    ordering = ["name"]  # 这样设置，publish是除id外的第一键


class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "register_time")
    list_filter = ("register_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    search_fields = ("name",)
    date_hierarchy = "register_time"  # 一个可以选择任意日期的过滤器
    ordering = ["name", "register_time"]  # 这样设置，publish是除id外的第一键


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("name", "register_time", "url")
    list_filter = ("register_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    search_fields = ("name",)
    date_hierarchy = "register_time"  # 一个可以选择任意日期的过滤器
    ordering = ["name", "register_time"]  # 这样设置，publish是除id外的第一键


class PsyTestAdmin(admin.ModelAdmin):
    list_display = ("name", "register_time", "url")
    list_filter = ("register_time",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    search_fields = ("name",)
    date_hierarchy = "register_time"  # 一个可以选择任意日期的过滤器
    ordering = ["name", "register_time"]  # 这样设置，publish是除id外的第一键

# admin.site.register(Consultant, ConsultantAdmin)
# admin.site.register(Lecture, LectureAdmin)
# admin.site.register(Resource, ResourceAdmin)
# admin.site.register(Articles, ArticlesAdmin)
# admin.site.register(PsyTest, PsyTestAdmin)
