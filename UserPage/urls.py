from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('auth/', views.auth,name='auth'),
    path('signup/', views.signup,name='signup'),
    path('signup/signin/', views.signin,name='signin'),
]