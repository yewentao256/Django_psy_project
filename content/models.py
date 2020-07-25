from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# 咨询师
class Consultant(models.Model):
    name = models.CharField(max_length=20, verbose_name="咨询师姓名")
    content = models.CharField(max_length=300, verbose_name="咨询师简介", blank=True)
    telephone = models.CharField(max_length=11, verbose_name="咨询师电话", blank=True)
    QQ = models.CharField(max_length=16, verbose_name="咨询师QQ", blank=True)
    register_time = models.DateTimeField(default=timezone.now, verbose_name="注册时间")

    class Meta:
        ordering = ("register_time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "一键咨询"
        verbose_name_plural = "一键咨询"

    def __str__(self):
        return self.name  # 对应后台文章列表中的默认显式字段


# 讲座信息
class Lecture(models.Model):
    name = models.CharField(max_length=20, verbose_name="讲座名称")
    content = models.CharField(max_length=300, verbose_name="讲座简介", blank=True)
    time = models.DateTimeField(default=timezone.now, verbose_name="开始时间")

    class Meta:
        ordering = ("time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "名家讲座"
        verbose_name_plural = "名家讲座"

    def __str__(self):
        return self.name  # 对应后台文章列表中的默认显式字段


# 资源获取
class Resource(models.Model):
    # 上传文件辅助函数
    def resource_path(self, filename):
        return "media/{0}/{1}".format(self.name, filename)

    name = models.CharField(max_length=20, verbose_name="资源名称")
    content = models.CharField(max_length=300, verbose_name="资源简介", blank=True)
    resource = models.FileField(verbose_name="资源上传", upload_to=resource_path,
                                help_text="直接上传到服务器，名称中不要有中文")

    register_time = models.DateTimeField(default=timezone.now, verbose_name="上传时间")

    class Meta:
        ordering = ("register_time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "书籍资源"
        verbose_name_plural = "书籍资源"

    def __str__(self):
        return self.name  # 对应后台文章列表中的默认显式字段


# 文章转载
class Articles(models.Model):
    name = models.CharField(max_length=20, verbose_name="文章名称")
    content = models.CharField(max_length=300, verbose_name="文章简介", blank=True)
    url = models.URLField(max_length=100, verbose_name="url路径", null=True)
    register_time = models.DateTimeField(default=timezone.now, verbose_name="上传时间")

    class Meta:
        ordering = ("register_time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "好文共赏"
        verbose_name_plural = "好文共赏"

    def __str__(self):
        return self.name  # 对应后台文章列表中的默认显式字段


# 测试链接
class PsyTest(models.Model):
    name = models.CharField(max_length=20, verbose_name="心理测试名称")
    content = models.CharField(max_length=300, verbose_name="测试简介", blank=True)
    url = models.URLField(max_length=100, verbose_name="url路径", null=True)
    register_time = models.DateTimeField(default=timezone.now, verbose_name="上传时间")

    class Meta:
        ordering = ("register_time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "趣味测试"
        verbose_name_plural = "趣味测试"

    def __str__(self):
        return self.name  # 对应后台文章列表中的默认显式字段
