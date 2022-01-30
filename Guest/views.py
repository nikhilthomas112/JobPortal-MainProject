from django.shortcuts import redirect, render, HttpResponse

from Admin.models import Country, State, District, Place
from .forms import EmployerForm


# Create your views here.
def index(request):
    return render(request, "Guest/base/base.html")


def employer_register(request):
    countries = Country.objects.all
    if request.method == "GET":
        print(countries)
        return render(request, "Guest/forms/employer_registration.html", {"countries": countries})
    else:
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Created!")
        else:
            print(str(form.errors))
            return render(request, "Guest/forms/employer_registration.html",
                          {
                              "countries": countries
                          })


def get_state(request):
    if request.method == "POST":
        country_id = request.POST.get('id')
        states = State.objects.filter(country=country_id)
        response = ""
        for state in states:
            response += str(state.id) + "," + str(state.state_name) + ";"
        return HttpResponse(response)


def get_district(request):
    if request.method == "POST":
        state_id = request.POST.get('id')
        districts = District.objects.filter(state=state_id)
        response = ""
        for district in districts:
            response += str(district.id) + "," + str(district.district_name) + ";"
        return HttpResponse(response)


def get_place(request):
    if request.method == "POST":
        district_id = request.POST.get('id')
        places = Place.objects.filter(district=district_id)
        response = ""
        for place in places:
            response += str(place.id) + "," + str(place.place_name) + ";"

        return HttpResponse(response)
