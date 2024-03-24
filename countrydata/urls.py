from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('comparison/', views.comparison, name='comparison'),
    path('about/', views.about, name='about'),
]