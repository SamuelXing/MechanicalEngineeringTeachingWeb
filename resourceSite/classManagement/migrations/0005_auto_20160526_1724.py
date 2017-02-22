# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classManagement', '0004_auto_20160526_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapters',
            name='image',
            field=models.ImageField(verbose_name='大章图片', upload_to='chap_img/%Y/%m/%d'),
        ),
    ]
