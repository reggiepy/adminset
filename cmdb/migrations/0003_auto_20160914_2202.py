# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-14 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_ipaddr'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net', models.CharField(max_length=30)),
                ('subnet', models.CharField(max_length=30, null=True)),
                ('describe', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Ipaddr',
        ),
    ]
