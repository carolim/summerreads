# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20150516_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='page_number',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
