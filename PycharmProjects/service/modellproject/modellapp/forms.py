from django import forms
from .models import FeedbackModel

# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     age = forms.IntegerField()
#     city = forms.CharField(max_length=30)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model =FeedbackModel
        fields = "__all__"