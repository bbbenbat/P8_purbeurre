from django.urls import path

from off_app import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    #path('', views.research_product, name="research_product"),
    path('addfavorite', views.create_favorite, name="addfavorite"),
]
