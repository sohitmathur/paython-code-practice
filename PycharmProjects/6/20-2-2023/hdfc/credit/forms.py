from django import forms
from.models import credit

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = credit
        fields='__all__'

