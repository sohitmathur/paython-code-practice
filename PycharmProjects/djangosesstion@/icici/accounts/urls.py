"""icici URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views

"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('saving/',views.saving_acc),
    path('current/',views.current_acc),
    path('cashcc/',views.cash_cc),
]
