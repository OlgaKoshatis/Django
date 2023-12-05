from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='home_page'),
    path('about/', views.about, name='about_me')
]