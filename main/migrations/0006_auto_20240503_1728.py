# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedbacks'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'verbose_name_plural': 'Softwares'},
        ),
        migrations.AlterModelOptions(
            name='tools',
            options={'verbose_name_plural': 'Tools'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name_plural': 'Versions'},
        ),
    ]
