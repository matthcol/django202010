from django.urls import path

from . import views
from .views import StarCreate, StarUpdate, StarDelete

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('star/', views.star, name='star'),
#    path('<str:title>/', views.by_title, name='by_title'),
    path('by_year/<int:year>/', views.by_year, name='by_year'),
#    CRUD
    path('star/add/', StarCreate.as_view(), name='star-add'),
    path('star/<int:pk>/update/', StarUpdate.as_view(), name='star-update'),
    path('star/<int:pk>/delete/', StarDelete.as_view(), name='star-delete'),
]
