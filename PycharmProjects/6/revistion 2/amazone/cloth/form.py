from django import forms


# Create your views here.
class StudentForm(forms.Form):
 name=forms.CharField()
 marks=forms.IntegerField()

<h1></h1>
