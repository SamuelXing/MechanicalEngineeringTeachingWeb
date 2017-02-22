# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blogManagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogManagement', '0002_auto_20160419_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.IntegerField(verbose_name='状态', default=0, choices=[(0, '发布'), (1, '草稿'), (2, '删除')]),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=blogManagement.models.NormalTextField(verbose_name='内容', blank=True, null=True),
        ),
    ]
