from django import forms
from .models import ShirtModel
class ShirtModel(forms.ModelForm):
    class Meta:
        model=ShirtModel
        fields="__all__"