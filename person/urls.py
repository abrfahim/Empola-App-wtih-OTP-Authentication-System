from django.urls import path
from . import views

app_name = 'person'

urlpatterns = [
    path('', views.makecard, name='register'),
    path('profile/', views.all_profile, name='all_profile'),
    path('delete_profile/<int:id>/', views.delete_profile, name='delete_profile'),
    path('update_profile/<int:id>/', views.update_profile, name='update_profile'),
]