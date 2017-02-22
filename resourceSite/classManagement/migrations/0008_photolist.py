# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0007_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='名称', max_length=50)),
                ('file', models.ImageField(verbose_name='图片文件', upload_to='detail/%Y/%m/%d')),
                ('created', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('photo', models.ForeignKey(verbose_name='所属图片类', to='classManagement.Photos', related_name='photo_list')),
            ],
            options={
                'verbose_name': '详细图片',
                'verbose_name_plural': '详细图片',
                'ordering': ['created'],
            },
        ),
    ]
