from django.urls import path

from . import views

urlpatterns = [
    path('accounts/employee/', views.employee_home, name="employee-home"),
    path('accounts/employee/applications/', views.applied_jobs, name="applied-jobs"),
    path('accounts/employee/profile/', views.view_profile, name="employee-profile"),
    path('accounts/employee/profile/edit', views.edit_profile, name="edit-employee-profile"),
    path('jobs/', views.search_jobs, name="search-jobs"),
    path('jobs/details/', views.job_details, name="job-info"),
    path('jobs/apply/', views.apply_job, name="apply-job"),
]
