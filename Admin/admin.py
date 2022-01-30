from django.contrib import admin

from Admin.models import AdminLogin, CourseType, Course, Country, State, District, Place

# Register your models here.
admin.site.register(AdminLogin)
admin.site.register(CourseType)
admin.site.register(Course)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Place)
