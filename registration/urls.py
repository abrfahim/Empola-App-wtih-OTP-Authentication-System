from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('register_user/', views.register_user, name='register_user'),
    path('reset/', views.reset, name='reset'),
    path('verify/', views.verify_account, name='verify_account'),
    path('logout_user/', views.logout_user, name='logout_user'),
]
