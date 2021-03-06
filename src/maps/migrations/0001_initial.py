# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VeterinaryPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('site_image', models.ImageField(height_field='height_field', upload_to='', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('snippet', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
