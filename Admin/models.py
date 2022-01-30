from django.db import models


# Create your models here.
# Admin login table
class AdminLogin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)


# Table for course type
class CourseType(models.Model):
    course_type = models.CharField(max_length=20)


# Table for Courses
class Course(models.Model):
    course_type_id = models.ForeignKey(CourseType, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=50)


# Table for Counties
class Country(models.Model):
    country_name = models.CharField(max_length=100)


# Table for States
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=50)


# Table for Districts
class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district_name = models.CharField(max_length=50)


# Table for Place
class Place(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=50)


