from django.forms import ModelForm, DateInput, NumberInput
from .models import Star, Movie

class MyDateInput(DateInput):
    input_type="date"

class StarForm(ModelForm):
    class Meta:
        model = Star
        fields = ['name', 'birthdate']
        # widgets = {
        #     'birthdate': MyDateInput()
        # }