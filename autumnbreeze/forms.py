from django import forms

from autumnbreeze.models import ComparingOption


class AnomalyForm(forms.Form):
    baseline_file = forms.FileField()
    file_to_compare = forms.FileField()
    comparing_option = forms.ModelChoiceField(
        queryset=ComparingOption.objects.all()
    )
