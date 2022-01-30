from django.contrib import admin

from Employer.models import Employer, Job, EmployeeInvite, Employee, ApplyJob

# Register your models here.
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(EmployeeInvite)

# Actually these are user models
admin.site.register(Employee)
admin.site.register(ApplyJob)
