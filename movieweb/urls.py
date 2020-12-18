from django.urls import path

from . import views
from .views import StarCreate, StarUpdate, StarDelete, MovieCreate, MovieUpdate

urlpatterns = [
# MOVIE urls
    path('', views.index, name='index'),
    path('movie/', views.movies, name='movies'),
    path('movie/<int:movie_id>/', views.movie, name='movie-info'),
    path('movie/by_year/', views.movies_by_year, name='movies-by-year'),
    # CRUD with forms
    path('movie/add/', MovieCreate.as_view(), name='movie-add'),
    path('movie/<int:pk>/update/', MovieUpdate.as_view(), name='movie-update'),
# STAR urls    
    path('star/', views.stars, name='stars'),
    path('star/<int:star_id>', views.star, name='star-info'),
    # CRUD with forms
    path('star/add/', StarCreate.as_view(), name='star-add'),
    path('star/<int:pk>/update/', StarUpdate.as_view(), name='star-update'),
    path('star/<int:pk>/delete/', StarDelete.as_view(), name='star-delete'),
]
