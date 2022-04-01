from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Employee, Employer

from MetaData.models import Country, CourseType


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "input100",
                "placeholder": "Enter mail id",
                "maxlength": "20"
            }
        ),
        label="E-mail"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100",
                "placeholder": "Enter Password"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100",
                "placeholder": "Re-enter Password"
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
            "class": "input100",
            "placeholder": "Company Name"
        })
        self.fields['place'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Select Location"
        })
        self.fields['company_type'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter Organization Category"
        })
        self.fields['about_company'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter about the organization"
        })
        self.fields['logo'].widget.attrs.update({
            'class': 'form-control',
            'style': 'border: none;'
        })

    class Meta:
        model = Employer
        fields = "__all__"


class EmployeeSignUpForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter First Name"
        })
        self.fields['last_name'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter Last Name"
        })
        self.fields['date_of_birth'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter DOB"
        })
        self.fields['contact'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter Mobile Number"
        })
        self.fields['experience'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter Experience"
        })
        self.fields['search_tags'].widget.attrs.update({
            "class": "input100",
            "placeholder": "Enter Search Tags"
        })
        self.fields['avatar_image'].widget.attrs.update({
            "class": "form-control input100 file",
            "placeholder": "Select Image",
            "style": "height: 35px; border: none;"
        })
        self.fields['resume'].widget.attrs.update({
            "class": "form-control input100 file",
            "placeholder": "Select Resume",
            "style": "height: 35px; border: none;"
        })

    class Meta:
        model = Employee
        fields = "__all__"


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "input100",
                "placeholder": "Enter mail id"
            }
        ),
        label="E-mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input100",
                "placeholder": "Enter Password"
            }
        )
    )

