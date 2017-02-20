# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_cpudata_serveruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpudata',
            name='cpuload',
            field=models.IntegerField(verbose_name='cpu使用率'),
        ),
        migrations.AlterField(
            model_name='cpudata',
            name='serviceid',
            field=models.IntegerField(verbose_name='主机id'),
        ),
        migrations.AlterField(
            model_name='cpudata',
            name='time',
            field=models.DateTimeField(verbose_name='监控时间'),
        ),
        migrations.AlterField(
            model_name='serveruser',
            name='serverUserName',
            field=models.CharField(verbose_name='服务器用户名', max_length=32),
        ),
        migrations.AlterField(
            model_name='serveruser',
            name='serverUserPasswd',
            field=models.CharField(verbose_name='服务器密码', max_length=32),
        ),
        migrations.AlterField(
            model_name='serveruser',
            name='serviceid',
            field=models.IntegerField(verbose_name='主机id'),
        ),
        migrations.AlterField(
            model_name='service',
            name='cpu',
            field=models.CharField(verbose_name='cpu', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='disk',
            field=models.CharField(verbose_name='磁盘', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='host',
            field=models.CharField(verbose_name='主机名称', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='ip',
            field=models.CharField(verbose_name='主机ip', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='mac',
            field=models.CharField(verbose_name='mac', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='mem',
            field=models.CharField(verbose_name='内存', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='model',
            field=models.CharField(verbose_name='服务器型号', max_length=32),
        ),
        migrations.AlterField(
            model_name='service',
            name='system',
            field=models.CharField(verbose_name='系统', max_length=32),
        ),
    ]
