"""dwback URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('account/', include('account.urls'), name='account'),
    path('good/', include('good.urls'), name='good'),
]
