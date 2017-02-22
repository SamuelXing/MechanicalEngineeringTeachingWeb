# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0008_photolist'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='assignment',
            field=models.TextField(blank=True, verbose_name='作业', null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='permission',
            field=models.BooleanField(verbose_name='会员观看?', default=True),
        ),
    ]
