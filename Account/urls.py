from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.create_user, name="index"),
    path('accounts/signup/', views.create_user, name="create-user"),
    path('accounts/user-profile/', views.register_employee, name="employee-signup"),
    path('accounts/employer-profile/', views.register_employer, name="employer-signup"),
]
