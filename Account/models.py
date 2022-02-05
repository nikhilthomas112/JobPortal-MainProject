from django.db import models
from django.contrib.auth.models import AbstractUser

from MetaData.models import Place, Course


# Create your models here.
class User(AbstractUser):
    is_app_admin = models.BooleanField('Is app admin', default=False)
    is_employer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact = models.BigIntegerField()
    location = models.ForeignKey(Place, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    experience = models.IntegerField()
    search_tags = models.CharField(max_length=400)
    avatar_image = models.ImageField(upload_to='avatars')
    resume = models.FileField(upload_to='resumes')


class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    company_type = models.CharField(max_length=50)
    about_company = models.TextField()
    status = models.CharField(max_length=10, default="pending")

    def __str__(self):
        return f'{self.company_name}, {self.place.place_name}, {self.company_type},' \
               f' {self.about_company}'
