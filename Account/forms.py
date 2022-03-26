from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Employee, Employer

from MetaData.models import Country, CourseType


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter mail id"
            }
        ),
        label="E-mail"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_app_admin', 'is_employee', 'is_employer')


class EmployerSignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployerSignUpForm, self).__init__(*args, **kwargs)
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
        self.fields['logo'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Employer
        fields = "__all__"


class EmployeeSignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['date_of_birth'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['contact'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['experience'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['search_tags'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['avatar_image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['resume'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = Employee
        fields = "__all__"


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter mail id"
            }
        ),
        label="E-mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

