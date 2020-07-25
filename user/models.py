from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils import timezone


class User(models.Model):
    # 上传文件辅助函数
    def upload_path(self, filename):
        return "files/user/{0}/{1}".format(self.id, filename)

    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=88, verbose_name="用户校验码", blank=True)
    username = models.CharField(max_length=20, verbose_name="用户名", unique=True)
    password = models.CharField(max_length=20, verbose_name="密码")
    name = models.CharField(max_length=8, verbose_name="真实姓名", default="未命名")
    user_nickname = models.CharField(max_length=30, verbose_name="昵称", default="未命名")
    idcard = models.CharField(max_length=18, verbose_name="身份证号码", unique=True, help_text="用户唯一标识之一",
                              null=True, blank=True)
    sex = models.CharField(max_length=4, blank=True, verbose_name="性别", default='0',
                           help_text="0未知，1男，2女", choices=(
        (u"2", u"2"),
        (u"1", u"1"),
        (u"0", u"0")))
    # birthday = models.DateTimeField(blank=True, verbose_name="生日", null=True, default=timezone.now)
    birthday = models.CharField(max_length=20, blank=True, verbose_name="生日", null=True, default=0)
    create_time = models.CharField(max_length=20, blank=True, verbose_name="注册时间", null=True,
                                   default=str(int(timezone.now().timestamp())))
    user_email = models.EmailField(blank=True, null=True, verbose_name="邮箱")
    # avatar = models.ImageField(verbose_name="头像", blank=True, upload_to=upload_path)
    avatar = models.CharField(max_length=300, verbose_name="头像绝对路径", blank=True, null=True,
                              default='files/avatar/default.jpg')
    signature = models.TextField(verbose_name="个性签名", max_length=300, blank=True, null=True,
                                 error_messages={"max_length": "最多不能多于300个字符"})
    mobile = models.CharField(max_length=11, verbose_name="电话号码", unique=True, help_text="用户唯一标识之一",
                              validators=[validators.RegexValidator(r"1[345678]\d{9}$", message="请输入正确的电话号码！")],
                              null=True, blank=True)
    user_status = models.CharField(max_length=4, verbose_name="用户验证状态", default="0",
                                   help_text="0未验证，1已验证普通用户，2咨询师", choices=(
        (u"2", u"2"),
        (u"1", u"1"),
        (u"0", u"0")))
    address = models.CharField(max_length=40, verbose_name="地址", blank=True, null=True)

    # 登录信息
    # last_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="最后一次登录IP")
    # last_login_date = models.DateTimeField(blank=True, verbose_name="最后一次登陆时间", default=timezone.now)

    # 查询返回值
    def __str__(self):
        return self.user_nickname

    class Meta:
        ordering = ("id",)
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


# 咨询师
class Consultant(models.Model):
    def upload_path(self, filename):
        return "files/user/{0}/{1}".format(self.id, filename)
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="对应用户", blank=True,
                             related_name="consultant", help_text="咨询师需要绑定一个用户")
    # name = models.CharField(max_length=10, verbose_name="咨询师姓名")
    grade = models.CharField(max_length=20, verbose_name="咨询师等级", help_text="比如二级心理咨询师")
    expertise = models.CharField(max_length=20, verbose_name="专长", help_text="比如善于处理青少年问题")
    training = models.CharField(max_length=40, verbose_name="专业", help_text="比如中科院心理所医学与心理咨询治疗专业硕士研究生")
    # avatar = models.ImageField(verbose_name="头像", blank=True, upload_to=upload_path)

    qq = models.CharField(max_length=16, verbose_name="咨询师QQ")
    create_time = models.CharField(max_length=20, blank=True, verbose_name="注册时间", null=True, default=0)

    class Meta:
        ordering = ("create_time",)  # publish的倒序排序。此处是元组，不要忘写后面的逗号
        verbose_name = "咨询师信息"
        verbose_name_plural = "咨询师信息"

    # 查询返回值
    def __str__(self):
        return self.user.user_nickname
