# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import classManagement.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='大章名称', max_length=100)),
                ('intro', models.CharField(verbose_name='大章介绍', blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('image', models.ImageField(verbose_name='大章图片', upload_to='chap_img/%Y/%m/%d')),
            ],
            options={
                'verbose_name': '大章信息',
                'verbose_name_plural': '大章信息',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='课程名', max_length=50)),
                ('intro', models.CharField(verbose_name='课程介绍', blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', classManagement.models.NormalTextField(verbose_name='内容', blank=True, null=True)),
                ('created', models.DateTimeField(verbose_name='回复时间', auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name='回复人', to=settings.AUTH_USER_MODEL, related_name='video_reply')),
            ],
            options={
                'verbose_name': '回复信息',
                'verbose_name_plural': '回复信息',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='小节名称', max_length=100)),
                ('intro', models.CharField(verbose_name='介绍', blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('chap', models.ForeignKey(verbose_name='所属大章', to='classManagement.Chapters', related_name='sec_chap')),
            ],
            options={
                'verbose_name': '小节信息',
                'verbose_name_plural': '小节信息',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='视频名称', max_length=100)),
                ('intro', models.CharField(verbose_name='介绍', blank=True, max_length=200, null=True)),
                ('image', models.ImageField(verbose_name='视频图片', upload_to='video_img/%Y/%m/%d')),
                ('video', models.FileField(verbose_name='视频', upload_to='video/%Y/%m/%d')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('hits', models.IntegerField(verbose_name='点击数', default=1)),
                ('permission', models.BooleanField(verbose_name='普通用户能否观看', default=True)),
                ('is_demo', models.BooleanField(verbose_name='是否为演示视频', default=True)),
                ('chap', models.ForeignKey(verbose_name='所属小节', to='classManagement.Section', related_name='video_sec')),
                ('user', models.ForeignKey(verbose_name='上传者', to=settings.AUTH_USER_MODEL, related_name='upload_author')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='reply',
            name='video',
            field=models.ForeignKey(verbose_name='所属视频', to='classManagement.Video'),
        ),
        migrations.AddField(
            model_name='chapters',
            name='course',
            field=models.ForeignKey(verbose_name='所属课程', to='classManagement.Courses', related_name='chap_course'),
        ),
    ]
