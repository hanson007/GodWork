# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.CharField(max_length=32, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xbaip')),
                ('mac', models.CharField(max_length=32, verbose_name=b'mac')),
                ('cpu', models.CharField(max_length=32, verbose_name=b'cpu')),
                ('mem', models.CharField(max_length=32, verbose_name=b'\xe5\x86\x85\xe5\xad\x98')),
                ('disk', models.CharField(max_length=32, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98')),
                ('system', models.CharField(max_length=32, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f')),
                ('model', models.CharField(max_length=32, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe5\x9e\x8b\xe5\x8f\xb7')),
            ],
        ),
    ]
