from django.urls import path
from . import views

urlpatterns = [
    # Path to Home Page
    path('', views.home, name="stag-home"),
    path('about/', views.about, name="stag-about"),
]