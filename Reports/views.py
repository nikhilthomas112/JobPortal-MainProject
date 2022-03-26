from django.db.models import Sum
from django.shortcuts import render, HttpResponse

from Employer.models import Job, Employer, Employee
from MetaData.models import Course


# Create your views here.
def employer_jobs(request):
    employers = Employer.objects.all()
    jobs = []
    for employer in employers:
        jobs.append(Job.objects.filter(employer=employer).count())
    for job in jobs:
        print(job)

    return render(request, 'reports/employer_jobs_report.html', {
        'employers': employers,
        'jobs': jobs
    })


def vacancy_employees(request):
    vacancy = Job.objects.aggregate(Sum('vacancies'))
    employee = Employee.objects.count()
    print("Vacancy", vacancy)
    return render(request, 'reports/vaccancies_employer_report.html', {
        'vacancy': vacancy['vacancies__sum'],
        'employee': employee
    })


def course_employee(request):

    courses = Course.objects.all()
    employees = []
    for course in courses:
        employees.append(Employee.objects.filter(course=course).count())

    return render(request, 'reports/course_wise_employee.html', {
        'courses': courses,
        'employees': employees
    })


def experience_employee(request):

    employees = Employee.objects.all()
    return render(request, 'reports/experience_employee.html', {
        'employees': employees
    })
