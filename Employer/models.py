import datetime

from django.db import models
from djmoney.models.fields import MoneyField

from MetaData.models import Course
from Account.models import Employer, Employee


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    post_date = models.DateField(default=datetime.date.today())
    salary = MoneyField(max_digits=14, decimal_places=2)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    experience = models.IntegerField()
    search_tags = models.CharField(max_length=400)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    vacancies = models.IntegerField()

    def __str__(self):
        return f'{self.job_title}, {self.vacancies}'


class ApplyJob(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.job.job_title}, {self.employee}'
