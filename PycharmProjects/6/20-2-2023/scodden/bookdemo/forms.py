from django import forms
from.models import BookDemoModel

class BookDemoForm(forms.ModelForm):
    class Meta:
        model=BookDemoModel
        fields= '__all__'