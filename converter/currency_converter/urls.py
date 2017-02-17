from django.conf.urls import url, include
from django.contrib import admin
from currency_converter import views


urlpatterns = [

    url(r'^$', views.home, name= 'home'),
    url(r'^home$', views.home, name='home'),
    url(r'^savu$', views.savu, name= 'buton'),
    
]
