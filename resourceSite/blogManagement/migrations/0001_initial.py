# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=50)),
                ('summary', models.CharField(verbose_name='摘要', max_length=200)),
                ('content', models.TextField(verbose_name='正文')),
                ('created_at', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('userName', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-created_at'],
            },
        ),
    ]
