from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dash_home, name='DashHome'),
    path('ajax/dash_getData', views.dash_getData, name='dash_getData'),


]
