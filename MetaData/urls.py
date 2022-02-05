from django.urls import path, include

from . import views

urlpatterns = [
    path('info/states', views.get_state, name="get-state"),
    path('info/districts', views.get_district, name="get-district"),
    path('info/places', views.get_place, name="get-place"),
    path('info/courses', views.get_course, name="get-course"),
]
