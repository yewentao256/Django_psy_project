from django.utils import timezone
from django.db import models


# Create your models here.
# 消息
from user.models import User


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="对应用户",
                             related_name="message", help_text="消息需要绑定一个用户")
    mood = models.CharField(max_length=4, verbose_name="心情", help_text="0开心，1平淡无奇，2难过",
                            choices=(
                                (u"0", u"0"),
                                (u"1", u"1"),
                                (u"2", u"2")))
    content = models.TextField(max_length= 300, verbose_name="消息内容")
    type = models.CharField(max_length=4, verbose_name="类型", help_text="0私人花园信息，1公共花园信息",
                            choices=(
                                (u"0", u"0"),
                                (u"1", u"1")))
    anonymity = models.CharField(max_length=4, verbose_name="匿名", help_text="0不匿名，1匿名（私人花园都不匿名）",
                            choices=(
                                (u"0", u"0"),
                                (u"1", u"1")))
    create_time = models.DateTimeField(default=timezone.now, verbose_name="发表时间")

    class Meta:
        ordering = ("create_time",)
        verbose_name = "心情消息"
        verbose_name_plural = "心情消息"

    def __str__(self):
        return str(self.id)


# 心情花园评论
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="对应用户",
                             related_name="comment")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="对应消息id",
                             related_name="comment", help_text="评论需要绑定消息")
    content = models.TextField(max_length= 300, verbose_name="消息内容")
    anonymity = models.CharField(max_length=4, verbose_name="匿名", help_text="0不匿名，1匿名",
                            choices=(
                                (u"0", u"0"),
                                (u"1", u"1")))
    create_time = models.DateTimeField(default=timezone.now, verbose_name="发表时间")

    class Meta:
        ordering = ("create_time",)
        verbose_name = "消息评论"
        verbose_name_plural = "消息评论"

    def __str__(self):
        return str(self.id)
