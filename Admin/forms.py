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
