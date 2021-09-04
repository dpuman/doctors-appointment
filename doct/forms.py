from django import forms
from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateDoctor(ModelForm):
    class Meta:
        model = Doctor

        fields = '__all__'
        exclude = ['user']
        widgets = {
            'year_of_degree': DateInput(),

        }
