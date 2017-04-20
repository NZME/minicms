# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, db_index=True, unique=True)),
                ('url', models.CharField(max_length=255, db_index=True, unique=True)),
                ('title', models.CharField(max_length=64, null=True, blank=True)),
                ('keywords', models.CharField(max_length=254, null=True, blank=True)),
                ('description', models.CharField(max_length=254, null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('container', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(related_name='page_name', to='minicms.Page')),
            ],
        ),
    ]
