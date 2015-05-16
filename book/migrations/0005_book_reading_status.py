# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_remove_book_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reading_status',
            field=models.CharField(default=b'WNT', max_length=3, choices=[(b'CUR', b'Currently Reading'), (b'FIN', b'Finished Reading'), (b'WNT', b'Want to Read')]),
        ),
    ]
