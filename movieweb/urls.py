from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>/', views.by_title, name='by_title'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('by_year/<int:year>/', views.by_year, name='by_year'),
]
