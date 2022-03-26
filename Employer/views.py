from django.db.models import Q

from django.shortcuts import render, redirect

from .models import Job, ApplyJob
from Account.models import Employer, Employee
from MetaData.models import Course, Country, Place

from .forms import NewJobForm


# Create your views here.
def employer_home(request):
    if request.user.is_authenticated and request.user.is_employer:
        return render(request, "base/employer/base.html")
    else:
        return redirect("index-page")


def view_jobs(request):
    if request.user.is_authenticated and request.user.is_employer:
        employer = Employer.objects.get(user=request.user)
        jobs = Job.objects.filter(employer=employer)
        return render(request, "views/employer/view_jobs.html", {"jobs": jobs})
    else:
        return redirect("index-page")


def job_details(request):
    if request.user.is_authenticated and request.user.is_employer:
        if request.method == "GET":
            jobid = request.GET.get('jobid', '')
            job = Job.objects.get(id=jobid)
            applicants = ApplyJob.objects.filter(job=job)
            for applicant in applicants:
                print("address :", applicant.employee.location.place_name,
                      applicant.employee.location.district.district_name,
                      applicant.employee.location.district.state.state_name,
                      applicant.employee.location.district.state.country.country_name)
            return render(request, "views/employer/job_details.html", {
                "jobs": job,
                "applicants": applicants
            })
    else:
        return redirect("index-page")


def applicant_details(request):
    if request.user.is_authenticated and request.user.is_employer:
        if request.method == "GET":
            applicant_id = request.GET.get('applicant', '')
            applicant = ApplyJob.objects.get(id=applicant_id)

            return render(request, "views/employer/applicant_details.html", {"applicant": applicant})
        else:
            status = request.POST.get('status')
            application_id = request.POST.get('application_id')
            application = ApplyJob.objects.get(id=application_id)
            application.status = status
            application.save()
            applicant = ApplyJob.objects.get(id=application_id)
            return render(request, "views/employer/applicant_details.html", {"applicant": applicant})
    else:
        return redirect("index-page")


def add_new_job(request):
    if request.user.is_authenticated and request.user.is_employer:
        employer = Employer.objects.get(user=request.user)
        if request.method == "GET":
            form = NewJobForm()
        else:
            form = NewJobForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view-jobs')
            print(form.errors)
        return render(request, "forms/employer/add_new_job.html", {
            'form': form,
            'employer': employer,
        })
    else:
        return redirect("index-page")


def search_employee(request):
    if request.user.is_authenticated and request.user.is_employer:
        courses = Course.objects.all
        if request.method == "GET":
            return render(request, "search/employer/search_employee.html", {'courses': courses})
        else:
            search_keyword = request.POST.get('search_keyword')
            search_course = request.POST.get('search_course')
            if search_course != "":
                course = Course.objects.get(id=search_course)
                employees = Employee.objects.filter(course=course)
            elif search_keyword != "":
                print("Inside keyword")
                employees = Employee.objects.filter(search_tags__icontains='{}'.format(search_keyword))

            return render(request, "search/employer/search_employee.html", {
                'courses': courses,
                'employees': employees
            })
    else:
        return redirect("index-page")


def view_employee_profile(request):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect("index-page")
    if request.method == "GET":
        employee_id = request.GET.get('employee')
        employee = Employee.objects.get(id=int(employee_id))
        return render(request, "views/employer/employee_profile.html", {'employee': employee})


def view_profile(request):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect("index-page")
    if request.method == "GET":
        employer = Employer.objects.get(user=request.user)
        return render(request, "views/employer/profile.html", {'employer': employer})


def edit_profile(request):
    if not request.user.is_authenticated or not request.user.is_employer:
        return redirect("index-page")
    employer = Employer.objects.get(user=request.user)
    countries = Country.objects.all
    if request.method == "POST":
        company_name = request.POST.get('company_name')
        company_type = request.POST.get('company_type')
        about_company = request.POST.get('about_company')
        place = request.POST.get('place')
        username = request.POST.get('username')
        password = request.POST.get('password1')

        location = Place.objects.get(id=int(place))

        employer = Employer.objects.get(user=request.user)
        employer.company_name = company_name
        employer.company_type = company_type
        employer.about_company = about_company
        employer.place = location
        employer.user.username = username
        employer.user.password = password

        employer.save()

    return render(request, "forms/employer/profile_update_form.html", {
        'employer': employer,
        'countries': countries
    })
