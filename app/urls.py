from django.urls import path
from . import views

urlpatterns = [
    # Path to Home Page
    path('', views.home, name="app-home"),
    path('about/', views.about, name="app-about"),
]