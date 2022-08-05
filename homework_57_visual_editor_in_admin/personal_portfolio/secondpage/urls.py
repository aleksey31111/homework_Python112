from django.urls import path

from . import views

urlpatterns = [
    path("", views.secondpage, name='secondpage'),
    path('<int:secondpage_id>/', views.detail, name="detail"),
]