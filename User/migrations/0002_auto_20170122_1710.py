# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(verbose_name='组名称', max_length=32),
        ),
        migrations.AlterField(
            model_name='method',
            name='name',
            field=models.CharField(verbose_name='权限名称', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='用户邮箱', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='用户密码', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(null=True, blank=True, verbose_name='用户手机', max_length=18),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, blank=True, verbose_name='用户头像', upload_to='image/userphoto'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(verbose_name='用户名称', max_length=32),
        ),
    ]
