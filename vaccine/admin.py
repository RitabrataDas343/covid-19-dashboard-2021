from django.contrib import admin
from .models import Vaccine

class VaccineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Vaccine, VaccineAdmin)
