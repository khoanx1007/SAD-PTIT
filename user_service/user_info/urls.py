from django import urls
from django.urls import path
from user_info import views

urlpatterns = [
    path('',views.user_info,),
]
