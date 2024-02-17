from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    city = forms.CharField(max_length=30)
