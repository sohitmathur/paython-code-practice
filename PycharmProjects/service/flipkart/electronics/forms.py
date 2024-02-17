from django import forms
from .models import MobileModel

class MobileForm(forms.ModelForm):
    class Meta:
        model= MobileModel
        fields = '__all__'
