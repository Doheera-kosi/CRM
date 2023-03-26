from django.urls import path
from . import views

urlpatterns = [
    # Creating new homepage
    path('', views.home, name='home'),
]
