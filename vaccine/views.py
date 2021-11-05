from cms.ajax_views import (AjaxDetailView, AjaxCreateView , AjaxUpdateView, AjaxDeleteView)
from cms.views import CoreListView
from .models import Vaccine
from .forms import VaccineForm


class VaccineList(CoreListView):
    model = Vaccine

class VaccineDetail(AjaxDetailView):
    model = Vaccine

class VaccineCreate(AjaxCreateView):
    model = Vaccine
    form_class = VaccineForm

class VaccineUpdate(AjaxUpdateView):
    model = Vaccine
    form_class = VaccineForm

class VaccineDelete(AjaxDeleteView):
    model = Vaccine
