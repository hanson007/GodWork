# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('time', models.DateTimeField(verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe6\x97\xb6\xe9\x97\xb4')),
                ('operation', models.CharField(max_length=128, verbose_name=b'\xe6\x93\x8d\xe4\xbd\x9c')),
                ('level', models.IntegerField(verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe7\xad\x89\xe7\xba\xa7')),
                ('type', models.CharField(max_length=16, verbose_name=b'\xe6\x97\xa5\xe5\xbf\x97\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
        ),
    ]
