from django import forms

from MetaData.models import CourseType, Course, Country, State, District, Place


class CourseTypeRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseTypeRegisterForm, self).__init__(*args, **kwargs)
        self.fields['course_type'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = CourseType
        fields = "__all__"


class CourseRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseRegisterForm, self).__init__(*args, **kwargs)
        self.fields['course_type_id'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['course_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Course
        fields = "__all__"


class CountryRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CountryRegisterForm, self).__init__(*args, **kwargs)
        self.fields['country_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Country
        fields = "__all__"


class StateRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StateRegisterForm, self).__init__(*args, **kwargs)
        self.fields['country'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['state_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = State
        fields = "__all__"


class DistrictRegisterForm(forms.ModelForm):

    choices = [
        ('', '-----------')
    ]

    countries = Country.objects.filter()
    for country in countries:
        choices.append((country.id, country.country_name))
    choices = tuple(choices)
    print(choices)

    country = forms.CharField(
        widget=forms.Select(
            choices=choices,
            attrs={
                "class": "form-control",
                "onchange": "getState()"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(DistrictRegisterForm, self).__init__(*args, **kwargs)
        self.fields['state'].widget.attrs.update({
            'class': 'form-control',
            "onchange": "getDistrict()"
        })
        self.fields['district_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = District
        fields = ('country', 'state', 'district_name')


class PlaceRegisterForm(forms.ModelForm):

    choices_country = choices_state = [
        ('', '-----------')
    ]

    countries = Country.objects.filter()
    for country in countries:
        choices_country.append((country.id, country.country_name))
    choices_country = tuple(choices_country)
    print(choices_country)

    country = forms.CharField(
        widget=forms.Select(
            choices=choices_country,
            attrs={
                "class": "form-control",
                "onchange": "getState()"
            }
        )
    )

    states = State.objects.filter()
    for state in states:
        choices_state.append((state.id, state.state_name))
    choices_state = tuple(choices_state)
    print(choices_state)

    state = forms.CharField(
        widget=forms.Select(
            choices=choices_state,
            attrs={
                "class": "form-control",
                "onchange": "getDistrict()"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(PlaceRegisterForm, self).__init__(*args, **kwargs)
        self.fields['district'].widget.attrs.update({
            'class': 'form-control',
            "onchange": "getPlace()"
        })
        self.fields['place_name'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Place
        fields = ('country', 'state', 'district', 'place_name')
