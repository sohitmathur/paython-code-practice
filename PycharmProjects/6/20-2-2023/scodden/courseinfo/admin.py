from django.contrib import admin
from .models import CourseInfoModel

# Register your models here.

class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ['cname','cduration','cfees','cmentor']

admin.site.register(CourseInfoModel,CourseInfoAdmin)
