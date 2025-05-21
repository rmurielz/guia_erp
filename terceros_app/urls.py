# terceros_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('third_party/create/', views.third_party_create, name='third_party_create'),
    path('branch/create/<int:third_party_id>/', views.branch_create, name='branch_create'),
    path('get_cities/', views.get_cities, name='get_cities'),
]