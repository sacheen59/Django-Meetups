from django import forms

from meetups.models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')