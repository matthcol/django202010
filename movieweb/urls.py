from django.urls import path

from . import views
from .views import StarCreate, StarUpdate, StarDelete

urlpatterns = [
# MOVIE urls
    path('', views.index, name='index'),
    path('movie/', views.movies, name='movies'),
    path('movie/<int:movie_id>/', views.movie, name='movie-detail'),
    path('movie/by_year/', views.movies_by_year, name='movies-by-year'),
# STAR urls    
    path('star/', views.stars, name='stars'),
    path('star/<int:star_id>', views.star, name='star-detail'),
    # CRUD with forms
    path('star/add/', StarCreate.as_view(), name='star-add'),
    path('star/<int:pk>/update/', StarUpdate.as_view(), name='star-update'),
    path('star/<int:pk>/delete/', StarDelete.as_view(), name='star-delete'),
]
