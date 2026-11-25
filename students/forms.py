from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'first_name',
            'last_name',
            'other_name',
            'gender',
            'date_of_birth',
            'classroom',
            'address',
            'passport',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }