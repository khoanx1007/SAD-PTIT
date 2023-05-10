from django import urls
from django.urls import path
from user_login import views

urlpatterns = [
    path('',views.user_login,),
]
