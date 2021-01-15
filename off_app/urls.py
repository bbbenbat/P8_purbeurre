from django.contrib import admin
from django.urls import path

from off_app import views

urlpatterns = [
    path('', views.research_product, name="research_product"),
]