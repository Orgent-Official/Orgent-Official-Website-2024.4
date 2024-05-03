# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_software'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('software', models.ForeignKey(to='main.Software')),
            ],
            options={
                'verbose_name_plural': 'versions',
            },
        ),
    ]
