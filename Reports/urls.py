from django.urls import path

from . import views

urlpatterns = [
    path('accounts/admin/reports/employer-jobs/', views.employer_jobs, name="employer-report"),
    path('accounts/admin/reports/vacancy-employee/', views.vacancy_employees, name="vacancy-employee-report"),
    path('accounts/admin/reports/course-employee/', views.course_employee, name="course-employee-report"),
    path('accounts/admin/reports/experience-employee/', views.experience_employee, name="experience-employee-report"),
]
