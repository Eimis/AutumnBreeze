# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComparingOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('baseline_days', models.PositiveSmallIntegerField(help_text='Number of days to compare from baseline file')),
                ('days_to_compare', models.PositiveSmallIntegerField(help_text='Number of days to compare from second file file')),
                ('fluctuation', models.PositiveSmallIntegerField(help_text='An adjustable number of fluctuation in percentage to calculate         fluctuation between two data sets. F. ex. if number 20 will be saved         in this field, when two files will be compared, the system will try         to track a 20% increase of lication_ids that were mentioned in a         particular day.')),
            ],
        ),
    ]
