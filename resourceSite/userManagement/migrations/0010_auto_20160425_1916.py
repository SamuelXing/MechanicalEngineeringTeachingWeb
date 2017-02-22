# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0009_remove_normalusers_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalusers',
            name='userName',
            field=models.CharField(verbose_name='用户名', max_length=50),
        ),
    ]
