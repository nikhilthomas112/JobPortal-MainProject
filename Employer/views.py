import datetime

from django.shortcuts import render, redirect

from .models import Job, ApplyJob
from Account.models import Employer

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
