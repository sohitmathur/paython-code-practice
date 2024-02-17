from django.contrib import admin
from. models import Student

# Register your models here.
class Student_Admin (admin.ModelAdmin):
    list_display = ['roll','name','email','date','mobile','per']


admin.site.register(Student,Student_Admin)
