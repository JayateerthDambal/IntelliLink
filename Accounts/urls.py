from django.urls import path
from . import views
urlpatterns = [
    path('',  views.home, name='Home'),
    path('login/', views.login_page, name='LoginPage'),
    path('signup/', views.signup_page, name='SignupPage'),
    path('logout/', views.logout_page, name='LogoutPage'),
]