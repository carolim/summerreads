# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_reading_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page_number', models.CharField(max_length=10)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='quotes',
            field=models.ManyToManyField(to='book.Quote', null=True, blank=True),
        ),
    ]
