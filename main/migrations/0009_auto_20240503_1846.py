# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_message_usertext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='usertext',
            new_name='touser',
        ),
    ]
