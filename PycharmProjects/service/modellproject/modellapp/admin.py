from django.contrib import admin
from. models import Student


class Student_Admin (admin.ModelAdmin):
    list_display = ['roll','name','email','date','mobile','per','year_in_school','test']


admin.site.register(Student,Student_Admin)
