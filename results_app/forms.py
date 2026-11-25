from django import forms
from .models import Result


class ResultForm(forms.ModelForm):

    class Meta:

        model = Result

        fields = [
            'student',
            'subject',
            'examination',
            'ca_score',
            'exam_score',
            'teacher_comment',
            'principal_comment',
        ]