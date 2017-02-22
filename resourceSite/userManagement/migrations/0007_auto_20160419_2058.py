# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0006_auto_20160419_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment',
            field=models.DecimalField(verbose_name='金额(元)', max_digits=10, decimal_places=2),
        ),
    ]
