# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node',
            options={'verbose_name_plural': '节点', 'ordering': ['-created'], 'verbose_name': '节点'},
        ),
        migrations.AlterModelOptions(
            name='plane',
            options={'verbose_name_plural': '版块', 'ordering': ['-created'], 'verbose_name': '版块'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': '回复', 'ordering': ['-created'], 'verbose_name': '回复'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': '帖子', 'ordering': ['-created'], 'verbose_name': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'verbose_name_plural': '投票', 'ordering': ['-occurrence_time'], 'verbose_name': '投票'},
        ),
        migrations.AlterField(
            model_name='reply',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='创建时间', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='down_vote',
            field=models.IntegerField(null=True, verbose_name='反对数', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='last_touched',
            field=models.DateTimeField(null=True, verbose_name='最后浏览时间', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='up_vote',
            field=models.IntegerField(null=True, verbose_name='赞同数', blank=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='updated',
            field=models.DateTimeField(null=True, verbose_name='更新时间', blank=True),
        ),
    ]
