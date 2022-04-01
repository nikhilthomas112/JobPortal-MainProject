from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, EmployeeSignUpForm, EmployerSignUpForm, UserLoginForm
from .models import Employer
from MetaData.models import Country, CourseType, Course


# Create your views here.
def index(request):
    courses = Course.objects.all
    return render(request, "index.html", {'courses': courses})


def create_user(request):
    msg = None
    checkbox_name = ""
    checkbox_id = ""
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_app_admin:
                login(request, user)
                return HttpResponse("Admin")
            elif user is not None and user.is_employer:
                login(request, user)
                print("User is employer")
                return redirect('employer-signup')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee-signup')
            else:
                msg = 'invalid credentials'

        else:
            print(form.errors)
            msg = 'form is not valid'
    else:
        user = request.GET.get('user', '')
        print("User = ", type(user))
        if user == "employer":
            checkbox_name = "is_employer"
            checkbox_id = "id_is_employer"
        if user == "employee":
            checkbox_name = "is_employee"
            checkbox_id = "id_is_employee"
        form = CreateUserForm()
    return render(request, 'forms/user_creation.html', {
        'form': form,
        'msg': msg,
        'checkbox_name': checkbox_name,
        'checkbox_id': checkbox_id
    })


def register_employee(request):
    if request.user.is_authenticated:
        print("User Authenticated")
        msg = None
        countries = Country.objects.all
        courses = CourseType.objects.all
        if request.method == 'POST':
            form = EmployeeSignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                msg = 'user created'
                return redirect('/')
            else:
                print(form.errors)
                msg = 'form is not valid'
        else:
            form = EmployeeSignUpForm()
        return render(request, 'forms/employee_registration.html', {
            'form': form,
            'msg': msg,
            'course_types': courses,
            'countries': countries
        })
    else:
        return HttpResponse("User is not authenticated")


def register_employer(request):
    if request.user.is_authenticated:
        countries = Country.objects.all
        courses = CourseType.objects.all

        if request.method == 'POST':
            form = EmployerSignUpForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                return redirect('/')
            else:
                print(form.errors)
        else:
            form = EmployerSignUpForm()
        return render(request, 'forms/employer_registration.html', {
            'form': form,
            'course_types': courses,
            'countries': countries
        })
    else:
        return HttpResponse("User is not authenticated")


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None and user.is_app_admin:
                login(request, user)
                return redirect('admin-home')
            elif user is not None and user.is_employer:
                employer = Employer.objects.get(user=user)

                print("User status is {}".format(employer.status))

                if employer.status == "pending" or employer.status == "rejected":
                    return HttpResponse("Employer account is not verified.")

                login(request, user)
                print("User is employer")
                return redirect("employer-home")
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect("employee-home")
    else:
        form = UserLoginForm()
    return render(request, "forms/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('index-page')
