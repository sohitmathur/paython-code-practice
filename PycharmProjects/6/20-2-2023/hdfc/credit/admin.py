from django.contrib import admin
from . models import employee

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['empid','empname','empsal']
admin.site.register(employee,EmpAdmin)
