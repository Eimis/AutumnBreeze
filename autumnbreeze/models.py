from django.db import models

from django.utils.translation import ugettext as _


class ComparingOption(models.Model):
    '''
    A Comparing option that can be selected when comparing two data sets (two
    different *.csv files). New ComparingOption instances can be created in
    Django admin and selected from a dropdown field when files are uploaded via
    front-end.
    '''
    location_name = models.CharField(max_length=100)
    baseline_days = models.PositiveSmallIntegerField(help_text=_(
        'Number of days to compare from baseline file.'
    ))
    days_to_compare = models.PositiveSmallIntegerField(help_text=_(
        'Number of days to compare from second file.'
    ))
    fluctuation = models.PositiveSmallIntegerField(help_text=_(
        'An adjustable number of fluctuation in percentage to calculate \
        fluctuation between two data sets. F. ex. if number 20 will be saved \
        in this field, when two files will be compared, the system will try \
        to track a 20% increase of location_ids that were mentioned in a \
        particular day.'
    ))

    def __unicode__(self):
        return (self.location_name + ' ('
                + str(self.baseline_days) + '/'
                + str(self.days_to_compare) + '/'
                + str(self.fluctuation) + '%)')
