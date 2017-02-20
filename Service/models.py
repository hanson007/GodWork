#coding:utf-8
from django.db import models


class Service(models.Model):
    host = models.CharField(max_length=32,verbose_name="主机名称")
    ip = models.CharField(max_length=32,verbose_name="主机ip")
    mac = models.CharField(max_length=32,verbose_name="mac")
    cpu = models.CharField(max_length=32,verbose_name="cpu")
    mem = models.CharField(max_length=32,verbose_name="内存")
    disk = models.CharField(max_length=32,verbose_name="磁盘")
    system = models.CharField(max_length=32,verbose_name="系统")
    model = models.CharField(max_length=32,verbose_name="服务器型号")


class CpuData(models.Model):
    serviceid = models.IntegerField(verbose_name="主机id")
    cpuload = models.IntegerField(verbose_name="cpu使用率")
    time = models.DateTimeField(verbose_name="监控时间")


class ServerUser(models.Model):
    serviceid = models.IntegerField(verbose_name="主机id")
    serverUserName = models.CharField(max_length=32,verbose_name="服务器用户名")
    serverUserPasswd = models.CharField(max_length=32,verbose_name="服务器密码")

# Create your models here.
