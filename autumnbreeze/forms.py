from django.conf import settings
from django import forms
from django.utils.translation import ugettext as _

from autumnbreeze.models import ComparingOption


class AnomalyForm(forms.Form):
    baseline_file = forms.FileField()
    file_to_compare = forms.FileField()
    comparing_option = forms.ModelChoiceField(
        queryset=ComparingOption.objects.all(),
    )

    def is_valid(self):
        valid = super(AnomalyForm, self).is_valid()
        # TODO: implement file format validation
        if ('baseline_file' in self.cleaned_data
                and self.cleaned_data[
                    'baseline_file'
                ] > settings.MAX_UPLOAD_SIZE):
            self.add_error('baseline_file', _(
                _('File exceeds max file size limit of 2.5 mb')
            ))

        if ('file_to_compare' in self.cleaned_data
                and self.cleaned_data[
                    'file_to_compare'
                ] > settings.MAX_UPLOAD_SIZE):
            self.add_error('file_to_compare', _(
                _('File exceeds max file size limit of 2.5 mb')
            ))

        return valid
