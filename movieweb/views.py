from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from django.forms import DateInput, NumberInput, DateField
from datetime import date
from .models import Movie, Star
from .forms import StarForm

def index(request):
    movie_count = Movie.objects.count()
    star_count = Star.objects.count()
    return render(request, 'movieweb/index.html', 
                  {'movie_count': movie_count, 'star_count': star_count,
                   'title': 'DBMovie Fanzone',
                   'now': date.today()})

def movies(request):
#    movies = [
#            {'title': 'Mulan', 'year':2020, 'duration': 75}, 
#            {'title':'No Time To Die', 'year':2021}, 
#            {'title':'Back To The Future', 'year': 1985}, 
#            {'title':'No Time To Die 3', 'year':2021}, 
#            {'title':'No Time To Die 4', 'year':2021}, 
#            ]
    movies = Movie.objects.all()
    return render(request, 'movieweb/movies.html', 
                  {'movies': movies, 'title': 'last news'})

def movie(request, movie_id):
    movie = Movie.objects \
        .select_related('director') \
        .prefetch_related('actors') \
        .get(pk=movie_id) 
    return render(request, 'movieweb/movie.html', {'movie':movie})

def movies_by_year(request, year=None):
    if year is None:
        year= request.GET.get('year')
    movies = Movie.objects.filter(year=year).order_by('title')
    return render(request, 'movieweb/movies.html', 
                  {'movies': movies, 'title': 'results'})

def movie_by_title(request, title):
    return HttpResponse(f"Movies with title: {title} (TODO)")


def stars(request):
    # stars = [
    #         {'name': 'Michael J. Fox', 'birthdate': date(1961,6,9)},
    #         {'name': 'Christopher Lloyd', 'birthdate': date(1938,10,22)},
    #         ]
    stars = Star.objects \
        .filter(birthdate__year__gt=1990) #.all() 
    return render(request, 'movieweb/stars.html', 
                  {'stars':stars, 'title': 'most famous'})

def star(request, star_id):
    star = Star.objects \
        .prefetch_related('directedMovies') \
        .prefetch_related('playedMovies') \
        .get(pk=star_id) 
    return render(request, 'movieweb/star.html', 
                  {'star':star})

class StarCreate(CreateView):
    model = Star
    # fields = ['name', 'birthdate']
    form_class=StarForm
    template_name='movieweb/star_form_add.html'
  
class StarUpdate(UpdateView):
    model = Star
    # fields = ['name', 'birthdate']
    form_class=StarForm
    template_name='movieweb/star_form_modify.html'
 
class StarDelete(DeleteView):
    model = Star
    success_url = reverse_lazy('stars')

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'year', 'duration', 'director']
    template_name='movieweb/movie_form_add.html'

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'year', 'duration', 'director', 'actors']
    template_name='movieweb/movie_form_modify.html'



