from django import forms

from Account.models import Employee


class EmployeeUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewJobForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['job_description'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['post_date'].widget.attrs.update({
            'class': 'form-control',
            'hidden': 'true'
        })
        self.fields['salary'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['course_name'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['experience'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['vacancies'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['search_tags'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Employee
        fields = "__all__"

