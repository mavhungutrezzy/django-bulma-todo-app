from django.urls import path
from todoapp import views


urlpatterns = [
    
    path('', views.home, name='home'),
]