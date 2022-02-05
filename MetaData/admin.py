from django.contrib import admin

from .models import Country, State, District, Place, CourseType, Course


# Register your models here.
admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Place)
admin.site.register(CourseType)
admin.site.register(Course)
