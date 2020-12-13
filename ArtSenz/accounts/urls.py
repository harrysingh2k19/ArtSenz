from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
            path('',views.index,name="index"),
            path('user_article',views.user_article,name="user_article"),
            path('add_article',views.add_article,name="add_article"),
            path('registration/', views.registration, name = 'registration'),
            path('article/<ide>',views.article,name="article"),  #Change

            ]
