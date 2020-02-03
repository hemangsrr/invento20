from django import forms
from .models import Event_register, Event

class EventRegisterForm(forms.ModelForm):

    class Meta:
            model = Event_register
            fields = [
                'first_name',
                'last_name',
                'email',
                'phone',
                'referal_code'
            ]

