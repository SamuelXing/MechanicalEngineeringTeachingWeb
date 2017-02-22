# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0005_auto_20160526_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='is_display',
            field=models.BooleanField(verbose_name='是否为图片展示', default=False),
        ),
    ]
