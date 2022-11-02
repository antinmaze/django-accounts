"""Account Urls"""
from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('password/', views.password, name='password'),
    path('', views.account, name='account'),
]

#manage access to the photos media
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
