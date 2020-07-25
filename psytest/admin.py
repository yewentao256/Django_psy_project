from django.contrib import admin
from .models import Questions
# Register your models here.

# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("id", "topic")
    list_filter = ("topic",)  # 以register_time增加一个过滤器，可以根据日期选择显示文章
    search_fields = ("topic",)
    date_hierarchy = "create_time"  # 一个可以选择任意日期的过滤器
    ordering = ["id", "topic"]  # 这样设置，publish是除id外的第一键


admin.site.register(Questions, QuestionsAdmin)