# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0002_auto_20160419_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normalusers',
            options={'verbose_name': '用户信息', 'ordering': ['-created_at'], 'verbose_name_plural': '用户信息'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '支付信息', 'ordering': ['-payed_at'], 'verbose_name_plural': '支付信息'},
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='id',
            field=models.UUIDField(primary_key=True, editable=False, serialize=False),
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='membership',
            field=models.BooleanField(default=False, verbose_name='会员?'),
        ),
    ]
