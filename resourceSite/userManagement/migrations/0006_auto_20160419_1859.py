# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0005_auto_20160419_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalusers',
            name='userName',
            field=models.CharField(verbose_name='昵称', max_length=50),
        ),
    ]
