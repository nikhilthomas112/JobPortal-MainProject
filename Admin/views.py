from django.shortcuts import render, redirect

from Account.models import Employer, Employee
from .forms import *


# Create your views here.
def admin_home(request):
    return render(request, "base/admin/base.html")


def view_new_employers(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        employers = Employer.objects.filter(status="pending")
        for employer in employers:
            print(employer)
        return render(request, 'views/admin/view_new_employers.html', {
            'employers': employers
        })
    else:
        return redirect('index-page')


def view_employer_details(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            employer_id = request.GET.get('employer')
            status = request.GET.get('status', '')
            employer = Employer.objects.get(id=employer_id)
            return render(request, 'views/admin/employer_details.html', {
                'employer': employer,
                'status': status
            })

    else:
        return redirect('index-page')


def employer_change_status(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            accept_id = request.GET.get('accept', None)
            reject_id = request.GET.get('reject', None)
            if accept_id is not None:
                employer = Employer.objects.get(id=accept_id)
                employer.status = "accepted"
                employer.save()
            else:
                employer = Employer.objects.get(id=reject_id)
                employer.status = "rejected"
                employer.save()
            return redirect('view-new-employers')
    else:
        return redirect('index-page')


def view_all_employees(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        employees = Employee.objects.all
        return render(request, 'views/admin/all_employees.html', {
            'employees': employees
        })
    else:
        return redirect('index-page')


def view_employee_details(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            employee_id = request.GET.get('employee')
            employee = Employee.objects.get(id=employee_id)
            return render(request, 'views/admin/employee_profile.html', {
                'employee': employee
            })
    else:
        return redirect('index-page')


def view_all_employers(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        employers = Employer.objects.all
        return render(request, 'views/admin/all_employers.html', {
            'employers': employers,
        })
    else:
        return redirect('index-page')


def view_course_type(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        course_types = CourseType.objects.all

        return render(request, 'views/admin/registration/course_type.html', {'course_types': course_types})

    else:
        return redirect('index-page')


def register_course_type(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = CourseTypeRegisterForm()

        if request.method == "POST":
            form = CourseTypeRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view-course-type')

        return render(request, 'forms/admin/course_type.html', {'form': form})

    else:
        return redirect('index-page')


def view_course(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            course_type_id = request.GET.get('type')
            course_type = CourseType.objects.get(id=course_type_id)
            courses = Course.objects.filter(course_type_id=course_type)

        return render(request, 'views/admin/registration/course.html', {'courses': courses})

    else:
        return redirect('index-page')


def register_course(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = CourseRegisterForm()

        if request.method == "POST":
            print("Registering Course")
            form = CourseRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/admin/view/courses/?type={}'.format(request.POST.get('course_type_id')))

        return render(request, 'forms/admin/courses.html', {'form': form})

    else:
        return redirect('index-page')


def view_country(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        countries = Country.objects.all

        return render(request, 'views/admin/registration/countries.html', {'countries': countries})

    else:
        return redirect('index-page')


def register_country(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = CountryRegisterForm()

        if request.method == "POST":
            print("Registering Country")
            form = CountryRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('view-countries')

        return render(request, 'forms/admin/country.html', {'form': form})

    else:
        return redirect('index-page')


def view_states(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            country_id = request.GET.get('country')
            country = Country.objects.get(id=country_id)
            states = State.objects.filter(country=country)

            for state in states:
                print(state)

        return render(request, 'views/admin/registration/states.html', {'states': states})

    else:
        return redirect('index-page')


def register_states(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = StateRegisterForm()

        if request.method == "POST":
            print("Registering State")
            form = StateRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/admin/view/country/states/?country={}'.format(request.POST.get('country')))

        return render(request, 'forms/admin/states.html', {'form': form})

    else:
        return redirect('index-page')


def view_districts(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            state_id = request.GET.get('state')
            state = State.objects.get(id=state_id)
            districts = District.objects.filter(state=state)

            for district in districts:
                print(district)

        return render(request, 'views/admin/registration/districts.html', {'districts': districts})

    else:
        return redirect('index-page')


def register_district(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = DistrictRegisterForm()

        if request.method == "POST":
            print("Registering District")
            form = DistrictRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/admin/view/country/states/districts/?state={}'
                                .format(request.POST.get('state')))

        return render(request, 'forms/admin/districts.html', {'form': form})

    else:
        return redirect('index-page')


def view_place(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        if request.method == "GET":
            district_id = request.GET.get('district')
            district = District.objects.get(id=district_id)
            places = Place.objects.filter(district=district)

            for place in places:
                print(place)

        return render(request, 'views/admin/registration/place.html', {'places': places})

    else:
        return redirect('index-page')


def register_place(request):
    if request.user.is_authenticated and request.user.is_app_admin:
        form = PlaceRegisterForm()

        if request.method == "POST":
            print("Registering Place")
            form = PlaceRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/admin/view/country/states/districts/places/?district={}'
                                .format(request.POST.get('district')))

        return render(request, 'forms/admin/place.html', {'form': form})

    else:
        return redirect('index-page')
