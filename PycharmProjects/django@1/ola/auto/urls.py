

from django.contrib import admin
from django.urls import path
from auto import views

urlpatterns = [

    path('auto/',views.auto_index),
]
