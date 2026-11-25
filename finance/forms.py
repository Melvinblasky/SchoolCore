from django import forms
from .models import Payment , FeeStructure


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            'student',
            'session',
            'term',
            'amount_paid',
            'payment_date',
            'reference'
        ]

        widgets = {
            'payment_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            )
        }

class FeeStructureForm(forms.ModelForm):

    class Meta:

        model = FeeStructure

        fields = [
            'classroom',
            'session',
            'term',
            'amount'
        ]