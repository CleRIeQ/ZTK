from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView

from main.views import *

urlpatterns = [
    path('', main_page, name='index'),
]
