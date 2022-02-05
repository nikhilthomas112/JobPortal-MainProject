from django.shortcuts import render, HttpResponse

from MetaData.models import State, District, Place, Course


# Create your views here.
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


def get_course(request):
    if request.method == "POST":
        course_type_id = request.POST.get('id')
        courses = Course.objects.filter(course_type_id=course_type_id)
        response = ""
        for course in courses:
            response += str(course.id) + "," + str(course.course_name)

        return HttpResponse(response)