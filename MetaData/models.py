from django.db import models


# Create your models here.
# Table for course type
class CourseType(models.Model):
    course_type = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.course_type}'


# Table for Courses
class Course(models.Model):
    course_type_id = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.course_name}'


# Table for Counties
class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.country_name}'


# Table for States
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.state_name}'


# Table for Districts
class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.district_name}'


# Table for Place
class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.place_name}'
