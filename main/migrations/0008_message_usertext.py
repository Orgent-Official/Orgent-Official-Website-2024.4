# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20240503_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='usertext',
            field=models.CharField(max_length=200, default=1),
            preserve_default=False,
        ),
    ]
