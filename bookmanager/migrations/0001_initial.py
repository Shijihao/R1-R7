# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('AuthorID', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=200)),
                ('Publisher', models.CharField(max_length=100)),
                ('PublishDate', models.DateField()),
                ('Price', models.IntegerField()),
                ('AuthorID', models.ForeignKey(to='bookmanager.Author')),
            ],
        ),
    ]
