from django.urls import path
from .views import VaccineList, VaccineDetail, VaccineCreate, VaccineUpdate, VaccineDelete

app_name = 'vaccine'
urlpatterns = [
    path('vaccine/', VaccineList.as_view(), name='todo-list'),
    path('vaccine/<int:pk>/',VaccineDetail.as_view(), name='todo-detail'),
    path('vaccine/create/', VaccineCreate.as_view(), name='todo-create'),
    path('vaccine/update/<int:pk>/', VaccineUpdate.as_view(), name='todo-update'),
    path('vaccine/delete/<int:pk>/', VaccineDelete.as_view(), name='todo-delete'),
]