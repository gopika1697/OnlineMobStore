# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20171004_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=15000)),
                ('ram', models.CharField(max_length=10)),
                ('battery', models.CharField(default='3000 mAh', max_length=10)),
                ('display_size', models.FloatField(default=5.0)),
                ('display_type', models.CharField(default='AMOLED', max_length=100)),
                ('processor', models.CharField(default='Snapdragon', max_length=200)),
                ('gpu', models.CharField(default='Adreno', max_length=40)),
                ('stockrom', models.CharField(default='Android', max_length=40)),
                ('internal_mem', models.CharField(default='64GB', max_length=50)),
                ('camera_primary', models.CharField(default='16MP,f/2.0', max_length=30)),
                ('album_logo', models.CharField(max_length=1000)),
                ('is_favorite', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Company')),
            ],
        ),
    ]
