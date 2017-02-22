# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='更新时间', null=True),
        ),
    ]
