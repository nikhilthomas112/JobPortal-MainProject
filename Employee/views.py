from django.shortcuts import render, redirect
from django.db.models import Q

from MetaData.models import Course, CourseType, Country, Place
from Employer.models import Job, ApplyJob
from Account.models import Employee


# Create your views here.
def employee_home(request):
    return render(request, "base/employee/base.html")


def search_jobs(request):
    courses = Course.objects.all
    if request.method == "POST":
        search_keyword = request.POST.get('search_keyword')
        search_course = request.POST.get('search_course')
        if search_course != "":
            course = Course.objects.get(id=search_course)
            print("Course:", course.course_name)
            jobs = Job.objects.filter(course_name=course)
            for job in jobs:
                print("JOB : ", job.job_title)
        elif search_keyword != "":
            print("Inside keyword")
            jobs = Job.objects.filter(
                Q(search_tags__icontains='{}'.format(search_keyword)) |
                Q(job_title__icontains='{}'.format(search_keyword))
            )
    else:
        jobs = {}
    return render(request, "search/jobs/search_jobs.html", {
        'jobs': jobs,
        'courses': courses
    })


def job_details(request):
    status = ""
    if request.method == "GET":
        job_id = request.GET.get('jobid')
        job = Job.objects.get(id=job_id)

    if request.user.is_authenticated and request.user.is_employee:
        authenticated = True
        employee = Employee.objects.get(user=request.user)
        print("JOB Id :", job_id)
        apply = ApplyJob.objects.filter(Q(job=job_id) & Q(employee=employee))
        is_applied = False
        if apply is not None:
            is_applied = True
            for i in apply:
                status = i.status
    else:
        authenticated = False
    return render(request, "views/employee/job_details.html", {
        'jobs': job,
        'is_authenticated': authenticated,
        'is_applied': is_applied,
        'status': status
    })


def apply_job(request):
    if request.user.is_authenticated and request.user.is_employee:
        if request.method == "GET":
            job_id = request.GET.get('jobid')
            employee = Employee.objects.get(user=request.user)
            job = Job.objects.get(id=int(job_id))
            apply = ApplyJob.objects.get_or_create(job=job, employee=employee)

            return redirect('/jobs/details/?jobid={}'.format(job_id))


def applied_jobs(request):
    if request.user.is_authenticated and request.user.is_employee:
        employee = Employee.objects.get(user=request.user)
        jobs_applied = ApplyJob.objects.filter(employee=employee)
        return render(request, "views/employee/applied_jobs.html", {'applied_jobs': jobs_applied})


def view_profile(request):
    if request.user.is_authenticated and request.user.is_employee:
        employee = Employee.objects.get(user=request.user)
        return render(request, 'views/employee/profile.html', {'employee': employee})
    else:
        return redirect("index")


def edit_profile(request):
    if request.user.is_authenticated and request.user.is_employee:
        employee = Employee.objects.get(user=request.user)
        course_types = CourseType.objects.all
        countries = Country.objects.all

        if request.method == "POST":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            date_of_birth = request.POST.get('date_of_birth')
            contact = request.POST.get('contact')
            location = request.POST.get('location')
            course = request.POST.get('course')
            experience = request.POST.get('experience')
            search_tags = request.POST.get('search_tags')
            username = request.POST.get('username')
            avatar_image = request.FILES.get('avatar_image')
            resume = request.FILES.get('resume')

            print("Course:", course)
            place = Place.objects.get(id=location)
            course = Course.objects.get(id=course)
            employee = Employee.objects.get(user=request.user)

            employee.first_name = first_name
            employee.last_name = last_name
            employee.date_of_birth = date_of_birth
            employee.contact = contact
            employee.location = place
            employee.course = course
            employee.experience = experience
            employee.search_tags = search_tags
            employee.user.username = username

            if avatar_image is not None:
                employee.avatar_image = avatar_image

            if resume is not None:
                employee.resume = resume

            employee.save()

            return redirect("employee-profile")

        return render(request, 'forms/employee/profile_update_form.html', {
            'employee': employee,
            'course_types': course_types,
            'countries': countries
        })
    else:
        return redirect("index")
