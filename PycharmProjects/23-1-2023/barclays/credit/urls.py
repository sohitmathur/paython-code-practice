"""barclays URL Configuration"""


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cardinfo/', views.credit_info),
]
