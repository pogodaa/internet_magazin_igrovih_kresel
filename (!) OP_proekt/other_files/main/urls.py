from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    # Приложение main
    path('', views.index, name='index'),

    path('autorization/', views.login_autoriz, name='autorization'),
    path('polit_konf/', views.politica_konf, name='polit_konf'),
    path('pers_dann/', views.sogl_obrabotka_pes_dannix, name='sogl_obrabotka_pes_dannix'),
    path('about_page/', views.about_page, name='about_page'),
    path('dos_opl/', views.dostavka_oplata, name='dostavka_oplata'),
    path('contacts/', views.kontakti_page, name='contacts'),

    path('<slug:category_slug>/', views.index, name='index'),
]

# TOVARS
# from django.urls import path

# from . import views

# app_name = 'tovars'

# urlpatterns = [
#     # Приложение tovars

#     # Каталог
#     # path('office_chairs/', views.office_chairs, name='office_chairs_page'),

    
#     path('<slug:category_slug>/', views.category_page, name='category_page'),



#     # # Детские
#     # path('product/<int:product_id>/', views.page_tov_detsk_burukids_first, name='BUROKIDS_first'),

#     path('product/<slug:product_slug>/', views.product_page, name='product_page'),
# ]