from django.urls import path

from . import views

urlpatterns = [
    path('accounts/admin/', views.admin_home, name="admin-home"),
    path('accounts/admin/new-employers/', views.view_new_employers, name="view-new-employers"),
    path('accounts/admin/new-employers/details/', views.view_employer_details, name="view-employers"),
    path('accounts/admin/new-employers/status/', views.employer_change_status, name="update-employer-status"),
    path('accounts/admin/all-employees/', views.view_all_employees, name="all-employees"),
    path('accounts/admin/all-employees/profile/', views.view_employee_details, name="employee-profile-view"),
    path('accounts/admin/all-employers/', views.view_all_employers, name="all-employers"),
    path('accounts/admin/view/course-types/', views.view_course_type, name="view-course-type"),
    path('accounts/admin/register/course-types/', views.register_course_type, name="register-course-type"),
    path('accounts/admin/view/courses/', views.view_course, name="view-courses"),
    path('accounts/admin/register/courses/', views.register_course, name="register-courses"),
]
