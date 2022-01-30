from django.forms.models import ModelForm

from Employer.models import Employer


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"
