from django.db import models
from djmoney.models.fields import MoneyField

from Admin.models import Place, Course


# Create your models here.
# Table for Employer
class Employer(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    company_type = models.CharField(max_length=50)
    about_company = models.TextField()
    status = models.CharField(max_length=10, default="pending")
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.company_name}, {self.place.place_name}, {self.company_type},' \
               f' {self.about_company}, {self.username}, {self.password}'


# Table for Employees
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    mail_id = models.EmailField()
    contact = models.BigIntegerField()
    location = models.ForeignKey(Place, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    experience = models.IntegerField()
    search_tags = models.CharField(max_length=400)
    avatar = models.ImageField(upload_to='avatars')
    resume = models.FileField(upload_to='resumes')


# Table for Jobs
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    post_date = models.DateField()
    salary = MoneyField(max_digits=14, decimal_places=2)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    experience = models.IntegerField()
    search_tags = models.CharField(max_length=400)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    vacancies = models.IntegerField()


# Table for inviting Employee
class EmployeeInvite(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


# Table for Applying Job
class ApplyJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
