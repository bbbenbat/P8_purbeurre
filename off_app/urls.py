from django.urls import path

from off_app import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('product_research', views.product_research, name="product_research"),

]
