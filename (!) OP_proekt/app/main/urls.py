from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    # Приложение main
    path('', views.index, name='index'),


        
    path('autorization/', views.login_autoriz, name='autorization'),

    path('polit_konf/', views.politica_konf, name='polit_konf'),
    path('pers_dann/', views.sogl_obrabotka_pes_dannix, name='sogl_obrabotka_pes_dannix'),
    path('about_company/', views.about_page, name='about_page'),
    path('dos_and_opl/', views.dostavka_oplata, name='dostavka_oplata'),
    path('contacts/', views.kontakti_page, name='contacts'),
]
