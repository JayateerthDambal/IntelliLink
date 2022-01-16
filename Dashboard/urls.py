from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.dash_home, name='DashHome'),
    path('ajax/dash_getData', views.dash_getData, name='dash_getData'),
    path('test/', views.humidCharts, name='testHumid'),
    path('ajax/dash_getHumidData', views.dash_getHumidData, name='dash_getHumidData'),
    path('api/', views.SensorDataList.as_view()),
    # path('api_view/^user=(?P<user>)$/', views.SenorListView.as_view()),

]
