from django import forms
from .models import UploadReportForm,Domian

class UploadingForm(forms.ModelForm):
    class Meta:
        model=UploadReportForm
        fields='__all__'

    project_domain = forms.ModelMultipleChoiceField(queryset=Domian.objects.all(),widget=forms.CheckboxSelectMultiple)

