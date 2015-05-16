# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20150516_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
