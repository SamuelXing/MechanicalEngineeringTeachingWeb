# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import blogManagement.models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0002_auto_20160419_1426'),
        ('blogManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', blogManagement.models.NormalTextField(verbose_name='评论时间', blank=True, null=True)),
                ('created_at', models.DateTimeField(verbose_name='发表于', auto_now_add=True)),
                ('author', models.ForeignKey(related_name='comment_author', blank=True, to='userManagement.NormalUsers', null=True)),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章', 'ordering': ['-is_top', '-pub_at', '-created_at']},
        ),
        migrations.AddField(
            model_name='blog',
            name='is_top',
            field=models.BooleanField(verbose_name='置顶', default=False),
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_at',
            field=models.DateTimeField(verbose_name='发布时间', default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.IntegerField(verbose_name='状态', choices=[(0, '正常'), (1, '草稿'), (2, '删除')], default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='update_at',
            field=models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='view_times',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(verbose_name='创建于', auto_now_add=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, to='blogManagement.Blog', null=True),
        ),
    ]
