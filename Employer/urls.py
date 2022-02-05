from django.urls import path

from . import views

urlpatterns = [
    path('accounts/employer/', views.employer_home, name="employer-home"),
    path('accounts/employer/jobs/', views.view_jobs, name="view-jobs"),
    path('accounts/employer/jobs/details/', views.job_details, name="job-details"),
    path('accounts/employer/jobs/applicants/details/', views.applicant_details, name="applicant-details"),
    path('accounts/employer/jobs/new/', views.add_new_job(), name="new-job"),
]
