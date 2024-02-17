from django import forms
class StudentRegistration(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    mobile_no=forms.IntegerField()
    key=forms.CharField(widget=forms.HiddenInput())
