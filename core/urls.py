"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('processdata.urls')),
    path('', include('app.urls')), 
    path('', include('vaccine.urls')),
]
