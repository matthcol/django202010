from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView ,DeleteView
from datetime import date
from .models import Movie, Star

def index(request):
#    movies = [
#            {'title': 'Mulan', 'year':2020, 'duration': 75}, 
#            {'title':'No Time To Die', 'year':2021}, 
#            {'title':'Back To The Future', 'year': 1985}, 
#            {'title':'No Time To Die 3', 'year':2021}, 
#            {'title':'No Time To Die 4', 'year':2021}, 
#            ]
    movies = Movie.objects.all()
    return render(request, 'movieweb/movies.html', 
                  {'movies': movies, 'title': 'Movie Fanzone'})

def detail(request, movie_id):
    return render(request, 'movieweb/movie.html', {'movie_id': movie_id})

def star(request):
    # stars = [
    #         {'name': 'Michael J. Fox', 'birthdate': date(1961,6,9)},
    #         {'name': 'Christopher Lloyd', 'birthdate': date(1938,10,22)},
    #         ]
    stars = Star.objects.all()
    return render(request, 'movieweb/star.html', {'stars':stars})

def by_year(request, year):
    movies = Movie.objects.filter(year=year).order_by('title')
    return render(request, 'movieweb/movies.html', 
                  {'movies': movies, 'title': 'Movie search results'})

def by_title(request, title):
    return HttpResponse(f"Movies with title: {title}")

#def by_genre(request, genre):
#    return HttpResponse(f"Movies with genre: {genre}")

class StarCreate(CreateView):
    model = Star
    fields = ['name', 'birthdate']

class StarUpdate(UpdateView):
    model = Star
    fields = ['name', 'birthdate']

class StarDelete(DeleteView):
    model = Star




