# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0003_auto_20160526_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapters',
            name='image',
            field=models.ImageField(upload_to='chap_img/%Y/%m/%d', width_field=180, height_field=120, verbose_name='大章图片'),
        ),
    ]
