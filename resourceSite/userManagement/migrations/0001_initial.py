# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('email', models.CharField(unique=True, max_length=50, verbose_name='邮件')),
                ('membership', models.BooleanField(default=False, verbose_name='是否会员')),
                ('userName', models.CharField(max_length=50, verbose_name='用户名')),
                ('userImage', models.CharField(max_length=50, verbose_name='用户头像', blank=True)),
                ('signature', models.CharField(max_length=200, verbose_name='用户签名')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name_plural': '文章',
                'ordering': ['-created_at'],
                'verbose_name': '文章',
            },
        ),
    ]
