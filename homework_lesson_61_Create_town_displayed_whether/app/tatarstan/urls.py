from django.urls import path
from .views import tatarstan

urlpatterns = [
    path('', tatarstan, name='tatarstan')
]
