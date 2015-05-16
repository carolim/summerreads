# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20150516_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 16, 16, 54, 12, 476316, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 16, 16, 54, 17, 555791, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
