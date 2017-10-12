# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 11:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='articles.Article')),
                ('hardhint', models.TextField(blank=True, max_length=4000)),
                ('mediumhint', models.TextField(blank=True, max_length=4000)),
                ('easyhint', models.TextField(blank=True, max_length=4000)),
            ],
            bases=('articles.article',),
        ),
    ]
