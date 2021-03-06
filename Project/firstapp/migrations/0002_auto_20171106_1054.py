# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 18:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=50)),
                ('orgCateg', models.CharField(max_length=50)),
                ('orgUni', models.CharField(max_length=100)),
                ('orgFoun', models.CharField(max_length=30)),
                ('orgLogo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniName', models.CharField(max_length=50)),
                ('uniLoca', models.CharField(max_length=50)),
                ('uniLogo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='suggestion',
        ),
        migrations.AddField(
            model_name='org',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.University'),
        ),
    ]
