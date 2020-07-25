from django.db import models

# Create your models here.
from django.utils import timezone


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.TextField(verbose_name="题目", max_length=100)
    create_time = models.DateTimeField(blank=True, verbose_name="上传时间", null=True, default=timezone.now)
    tend = models.CharField(max_length=4, verbose_name="倾向",
                            help_text="0内向/外向，1实感/直觉，2思考/情感，3判断/知觉",
                            choices=(
                                (u"0", u"0"),
                                (u"1", u"1"),
                                (u"2", u"2"),
                                (u"3", u"3")))
    choose1 = models.TextField(max_length=100, verbose_name="选项1", help_text="注意，选项1对应左侧倾向")
    choose2 = models.TextField(max_length=100, verbose_name="选项2", help_text="注意，选项2对应右侧倾向")

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ("id",)
        verbose_name = "测试题目"
        verbose_name_plural = "测试题目"
