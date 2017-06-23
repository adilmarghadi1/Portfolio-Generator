# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 20:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('date_of_birth', models.DateField()),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.SmallIntegerField(default='')),
                ('small_bio', models.CharField(blank=True, default='', max_length=200)),
                ('main_bio', models.CharField(default='', max_length=600)),
                ('skill1', models.CharField(default='', max_length=100)),
                ('skill2', models.CharField(default='', max_length=100)),
                ('skill3', models.CharField(blank=True, default='', max_length=100)),
                ('skill4', models.CharField(blank=True, default='', max_length=100)),
                ('skill5', models.CharField(blank=True, default='', max_length=100)),
                ('skill6', models.CharField(blank=True, default='', max_length=100)),
                ('facebook', models.CharField(default='', max_length=500)),
                ('github', models.CharField(blank=True, default='', max_length=500)),
                ('twitter', models.CharField(blank=True, default='', max_length=500)),
                ('linkedin', models.CharField(blank=True, default='', max_length=500)),
                ('blog', models.CharField(blank=True, default='', max_length=500)),
                ('project1_name', models.CharField(default='', max_length=500)),
                ('project1_url', models.CharField(default='', max_length=500)),
                ('project1_description', models.CharField(default='', max_length=300)),
                ('project2_name', models.CharField(blank=True, default='', max_length=500)),
                ('project2_url', models.CharField(blank=True, default='', max_length=500)),
                ('project2_description', models.CharField(blank=True, default='', max_length=300)),
                ('project3_name', models.CharField(blank=True, default='', max_length=500)),
                ('project3_url', models.CharField(blank=True, default='', max_length=500)),
                ('project3_description', models.CharField(blank=True, default='', max_length=300)),
                ('date_created', models.DateField(blank=True)),
                ('time_created', models.TimeField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
