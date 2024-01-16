from .models import Tour
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['place','priority','date','image']