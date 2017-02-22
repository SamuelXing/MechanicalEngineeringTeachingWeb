# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0006_courses_is_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='图片名称', max_length=50)),
                ('intro', models.CharField(verbose_name='图片描述', max_length=200)),
                ('file', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='图片文件')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('chap', models.ForeignKey(verbose_name='所属小节', to='classManagement.Section', related_name='photo_sec')),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': '图片信息',
                'verbose_name_plural': '图片信息',
            },
        ),
    ]
