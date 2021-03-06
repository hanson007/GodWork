#coding:utf-8
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名称")
    password = models.CharField(max_length=32,verbose_name="用户密码")
    email = models.EmailField(verbose_name="用户邮箱")
    phone = models.CharField(max_length=18,verbose_name="用户手机",blank=True,null=True)
    photo = models.ImageField(upload_to="image/userphoto",verbose_name="用户头像",blank=True,null=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    name = models.CharField(max_length=32,verbose_name="组名称")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Method(models.Model):
    name = models.CharField(max_length=32, verbose_name="权限名称")
    users = models.ManyToManyField(User)
    groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.name


# Create your models here.
