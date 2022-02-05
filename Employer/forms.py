from django import forms

from .models import Job


class NewJobForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewJobForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['place'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['company_type'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['about_company'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Job
        fields = "__all__"
