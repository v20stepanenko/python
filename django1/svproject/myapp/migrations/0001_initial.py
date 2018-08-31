# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10)),
                ('vendor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Person'),
        ),
    ]