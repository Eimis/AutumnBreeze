# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autumnbreeze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparingoption',
            name='location_name',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comparingoption',
            name='fluctuation',
            field=models.PositiveSmallIntegerField(help_text='An adjustable number of fluctuation in percentage to calculate         fluctuation between two data sets. F. ex. if number 20 will be saved         in this field, when two files will be compared, the system will try         to track a 20% increase of location_ids that were mentioned in a         particular day.'),
        ),
    ]
