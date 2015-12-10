# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-10 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('version', models.CharField(max_length=50)),
                ('commits', models.IntegerField(default=0)),
                ('changeset_url', models.TextField()),
                ('pypi_url', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('name', 'version')]),
        ),
    ]
