from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dash_home, name='DashHome'),
    path('ajax/dash_getData', views.dash_getData, name='dash_getData'),
    path('ajax/chart_data', views.chart_data_rendering, name='chart_data'),

]
