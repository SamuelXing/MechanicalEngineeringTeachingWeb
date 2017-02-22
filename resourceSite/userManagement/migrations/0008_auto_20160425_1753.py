# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0007_auto_20160419_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normalusers',
            name='userImage',
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
