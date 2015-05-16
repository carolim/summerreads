# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20150516_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='start_date',
        ),
    ]
