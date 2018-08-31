# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-06 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='mainapp.Category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=20, verbose_name='Название продукта'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='category',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='category',
            name='manufacturer',
            field=models.ManyToManyField(to='mainapp.Manufacturer', verbose_name='Производители'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='client',
            field=models.CharField(max_length=20, verbose_name='Клиенты'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='partnership',
            field=models.CharField(max_length=20, verbose_name='Парнеры'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufacturer',
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ManyToManyField(to='mainapp.Manufacturer', verbose_name='Производители'),
        ),
    ]
