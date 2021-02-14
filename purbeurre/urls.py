"""purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts import views as vws
from researches import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # new
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),  # new
    path('', include('researches.urls')),  # new
    path('product_research/', views.product_research, name="product_research"),
    path('favorite_product', views.favorite_product, name="favorite_product"),
    path('favorite_save', views.favorite_save, name="favorite_save"),
    path('favorite_update', views.favorite_update, name="favorite_update"),
    path('info_product', views.info_product, name="info_product"),
    path('legal', views.legal, name="legal"),
    path('profil_user', views.profil_user, name="profil_user"),
    path('signup_user', vws.user_image_view, name='signup_user'),
    path('success', vws.success, name='success'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
