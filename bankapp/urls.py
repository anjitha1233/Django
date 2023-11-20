from django.contrib import admin
from django.urls import path
from . import views
app_name='bankapp'
urlpatterns = [
    path('', views.home,name='home'),
    # path('formapply', views.formapply,name='formapply'),

    ]

