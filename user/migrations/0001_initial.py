# Generated by Django 2.2.4 on 2020-05-25 16:35

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("token", models.CharField(blank=True, max_length=88, verbose_name="用户校验码")),
                ("username", models.CharField(max_length=20, verbose_name="用户名")),
                ("password", models.CharField(max_length=20, verbose_name="密码")),
                ("user_nickname", models.CharField(max_length=8, verbose_name="昵称")),
                ("sex", models.CharField(blank=True, choices=[("2", "2"), ("1", "1"), ("0", "0")], help_text="0未知，1男，2女", max_length=4, verbose_name="性别")),
                ("birthday", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name="生日")),
                ("create_time", models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name="注册时间")),
                ("user_email", models.EmailField(blank=True, max_length=254, null=True, verbose_name="邮箱")),
                ("avatar", models.ImageField(blank=True, upload_to=user.models.User.upload_path, verbose_name="头像")),
                ("signature", models.TextField(blank=True, error_messages={"max_length": "最多不能多于300个字符"}, max_length=300, null=True, verbose_name="个性签名")),
                ("mobile", models.CharField(help_text="用户唯一标识之一", max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator("1[345678]\\d{9}$", message="请输入正确的电话号码！")], verbose_name="电话号码")),
                ("user_status", models.CharField(choices=[("2", "2"), ("1", "1"), ("0", "0")], help_text="0未验证，1已验证普通用户，2咨询师", max_length=4, verbose_name="用户验证状态")),
                ("last_ip", models.GenericIPAddressField(blank=True, null=True, verbose_name="最后一次登录IP")),
                ("last_login_date", models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name="最后一次登陆时间")),
            ],
            options={
                "verbose_name": "用户信息",
                "verbose_name_plural": "用户信息",
                "ordering": ("id",),
            },
        ),
    ]