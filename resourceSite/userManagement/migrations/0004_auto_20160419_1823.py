# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0003_auto_20160419_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalusers',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
