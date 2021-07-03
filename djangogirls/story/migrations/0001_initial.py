# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(null=True)),
                ('post_url', models.URLField()),
                ('image', models.ImageField(null=True, upload_to='stories/')),
                ('created', models.DateField(auto_now_add=True)),
                ('is_story', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
            },
        ),
    ]
