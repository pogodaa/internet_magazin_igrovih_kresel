"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from main import views

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # main
    path('', include('main.urls', namespace='main')),

    # Страница товара
    path('catalog/product/<slug:product_slug>/', views.product_page, name='product_page'),

    # Поиск
    path('catalog/search/', views.catalog_page, name='search'),
    
    # Страница категории
    path('catalog/<slug:catalog_slug>/', views.catalog_page, name='catalog_page'),
    # path('catalog/<slug:catalog_slug>/<int:page>/', views.catalog_page, name='catalog_page'),

]

if settings.DEBUG:
      urlpatterns += [
            path("__debug__/", include("debug_toolbar.urls")),
      ]
      urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)