from django import forms

from .models import Job


class NewJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewJobForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['job_description'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['post_date'].widget.attrs.update({
            'class': 'input100',
            'hidden': 'true'
        })
        self.fields['salary'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['course_name'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['experience'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['vacancies'].widget.attrs.update({
            'class': 'input100'
        })
        self.fields['search_tags'].widget.attrs.update({
            'class': 'input100'
        })

    class Meta:
        model = Job
        fields = "__all__"

