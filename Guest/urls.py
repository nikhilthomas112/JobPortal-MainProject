from django.urls import path
from Guest import views

urlpatterns = [
    path('', views.index),
    path('register_employer/', views.employer_register),
    path('get-state', views.get_state),
    path('get-district', views.get_district),
    path('get-place', views.get_place),
]
