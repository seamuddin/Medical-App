from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('add_appointment/', add_appointment, name='appointment-add'),
    path('appointment/', appintment, name='appointment'),
]