from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "other_names": "Other Names",
            "date_of_birth": "Date of Birth",
            "gender": "Gender",
            "parent_first_name": "Parent First Name",
            "parent_last_name": "Parent Last Name",
            "parent_other_names": "Parent Other Names",
            "parent_email": "Parent Email",
            "parent_phone_number_1": "Parent Phone Number 1",
            "parent_phone_number_2": "Parent Phone Number 2",
            "parent_occupation": "Parent Occupation",
            "address": "Address",
            "address_1": "Address 1",
            "city": "City",
            "class_assigned": "Class Assigned",
            "date_enrolled": "Date Enrolled",
        }

        widgets = {
            "profile_picture": forms.ClearableFileInput(
                attrs={"class": "form-control", "placeholder": "Profile Picture"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "other_names": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Other Names"}
            ),
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "placeholder": "Date of Birth",
                }
            ),
            "gender": forms.Select(
                choices=[('Male', 'Male'), ('Female', 'Female')],
                attrs={"class": "form-control", "placeholder": "Gender"}
            ),
            "class_assigned": forms.Select(
                attrs={"class": "form-control", "placeholder": "Class Assigned"}
            ),
            "parent_first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent First Name"}
            ),
            "parent_last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent Last Name"}
            ),
            "parent_other_names": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent Other Names"}
            ),
            "parent_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Parent Email"}
            ),
            "parent_phone_number_1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent Phone Number 1"}
            ),
            "parent_phone_number_2": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent Phone Number 2"}
            ),
            "parent_occupation": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Parent Occupation"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Address"}
            ),
            "address_1": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Address 1"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "City"}
            ),
            "date_enrolled": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "placeholder": "Date Enrolled",
                }
            ),
        }
