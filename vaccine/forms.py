from django import forms
from cms.forms import BootstrapHelperForm
from .models import Vaccine


class VaccineForm(BootstrapHelperForm, forms.ModelForm):

    class Meta:
        model = Vaccine
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
