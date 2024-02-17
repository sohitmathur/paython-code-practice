from django import forms
from.models import StudRegistration,CourseInfoModel



class StudRegForm(forms.ModelForm):
    class Meta:
        model=StudRegistration
        fields = '__all__'

class CourseInfoForm(forms.ModelForm):
    class Meta:
        model=CourseInfoModel
        fields = '__all__'