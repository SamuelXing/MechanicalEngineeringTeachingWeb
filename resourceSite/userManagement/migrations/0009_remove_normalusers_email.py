# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0008_auto_20160425_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalusers',
            name='email',
        ),
    ]
