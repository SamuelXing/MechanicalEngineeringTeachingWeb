# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0002_courses_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapters',
            options={'ordering': ['created'], 'verbose_name': '大章信息', 'verbose_name_plural': '大章信息'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['created'], 'verbose_name': '课程信息', 'verbose_name_plural': '课程信息'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['created'], 'verbose_name': '小节信息', 'verbose_name_plural': '小节信息'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['created'], 'verbose_name': '视频信息', 'verbose_name_plural': '视频信息'},
        ),
        migrations.AddField(
            model_name='courses',
            name='status',
            field=models.IntegerField(choices=[(0, '发布'), (1, '草稿'), (2, '删除')], default=0, verbose_name='状态'),
        ),
    ]
