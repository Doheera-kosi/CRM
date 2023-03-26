from django.urls import path
from . import views

urlpatterns = [
    # Creating new homepage
    path('', views.home, name='home'),
    # path('login/', views.login_uesr, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
