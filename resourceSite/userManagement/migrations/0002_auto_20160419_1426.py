# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('payment', models.DecimalField(decimal_places=2, verbose_name='金额', max_digits=10)),
                ('payed_at', models.DateTimeField(verbose_name='成为会员时间')),
            ],
            options={
                'ordering': ['-payed_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='normalusers',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='normalusers',
            name='password',
        ),
        migrations.AddField(
            model_name='normalusers',
            name='user',
            field=models.OneToOneField(related_name='user', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='email',
            field=models.EmailField(verbose_name='邮件', unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='id',
            field=models.UUIDField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='signature',
            field=models.CharField(verbose_name='签名', max_length=200),
        ),
        migrations.AlterField(
            model_name='normalusers',
            name='userImage',
            field=models.URLField(blank=True, verbose_name='用户头像', max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(to='userManagement.NormalUsers'),
        ),
    ]
