# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blogManagement', '0003_auto_20160419_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comment_author', blank=True, null=True),
        ),
    ]
