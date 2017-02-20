# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='level',
            field=models.IntegerField(verbose_name='日志等级'),
        ),
        migrations.AlterField(
            model_name='log',
            name='operation',
            field=models.CharField(verbose_name='操作', max_length=128),
        ),
        migrations.AlterField(
            model_name='log',
            name='time',
            field=models.DateTimeField(verbose_name='日志时间'),
        ),
        migrations.AlterField(
            model_name='log',
            name='type',
            field=models.CharField(verbose_name='日志类型', max_length=16),
        ),
        migrations.AlterField(
            model_name='log',
            name='user',
            field=models.CharField(verbose_name='用户名称', max_length=32),
        ),
    ]
