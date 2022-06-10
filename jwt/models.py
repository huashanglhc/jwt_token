from django.db import models


class User(models.Model):

    username = models.CharField(max_length=64, verbose_name="用户名")
    pwd = models.CharField(max_length=64, verbose_name="密码")
    token = models.CharField(null=True, verbose_name="用户token", max_length=128)

    class Meta:
        db_table = "user"
        verbose_name = "用户表"

