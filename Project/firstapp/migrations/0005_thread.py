# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 21:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0004_remove_org_orguni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userDownVotes', models.ManyToManyField(blank=True, related_name='threadDownVotes', to=settings.AUTH_USER_MODEL)),
                ('userUpVotes', models.ManyToManyField(blank=True, related_name='threadUpVotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
