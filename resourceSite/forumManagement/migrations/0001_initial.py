# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import forumManagement.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(null=True, max_length=200, verbose_name='节点名称', blank=True)),
                ('introduction', models.CharField(null=True, max_length=500, verbose_name='介绍', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('topic_count', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(null=True, max_length=200, verbose_name='名称', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('content', forumManagement.models.NormalTextField(null=True, verbose_name='内容', blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('up_vote', models.IntegerField(null=True, blank=True)),
                ('down_vote', models.IntegerField(null=True, blank=True)),
                ('last_touched', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(related_name='reply_author', verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=160, verbose_name='标题')),
                ('content', models.TextField(null=True, verbose_name='帖子内容', blank=True)),
                ('hits', models.IntegerField(default=1, verbose_name='点击数')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated', models.DateTimeField(null=True, verbose_name='更新时间', blank=True)),
                ('reply_count', models.IntegerField(null=True, verbose_name='回复数量', blank=True)),
                ('up_vote', models.IntegerField(null=True, verbose_name='赞同', blank=True)),
                ('down_vote', models.IntegerField(null=True, verbose_name='反对', blank=True)),
                ('last_replied_time', models.DateTimeField(null=True, verbose_name='最后回复时间', blank=True)),
                ('last_touched', models.DateTimeField(null=True, verbose_name='最后点击时间', blank=True)),
                ('author', models.ForeignKey(related_name='topic_author', verbose_name='发帖人', to=settings.AUTH_USER_MODEL)),
                ('node', models.ForeignKey(to='forumManagement.Node', null=True, verbose_name='所属节点', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.IntegerField(null=True, verbose_name='状态', blank=True)),
                ('involved_type', models.IntegerField(null=True, blank=True)),
                ('occurrence_time', models.DateTimeField(null=True, blank=True)),
                ('involved_reply', models.ForeignKey(related_name='vote_reply', null=True, to='forumManagement.Reply', blank=True)),
                ('involved_topic', models.ForeignKey(related_name='vote_topic', null=True, to='forumManagement.Topic', blank=True)),
                ('involved_user', models.ForeignKey(related_name='vote_user', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('trigger_user', models.ForeignKey(related_name='vote_trigger', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(to='forumManagement.Topic', null=True, verbose_name='回复话题', blank=True),
        ),
        migrations.AddField(
            model_name='node',
            name='plane',
            field=models.ForeignKey(to='forumManagement.Plane', null=True, verbose_name='所属版块', blank=True),
        ),
    ]
