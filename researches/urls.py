from django.urls import path


from researches import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    #path('', views.main_page, name="main_page"),
    path('product_research', views.product_research, name="product_research"),
    path('favorite_product', views.favorite_product, name="favorite_product"),
]
