from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


def index(request):
    movies = [ 
            {'title': 'Mulan', 'year':2020, 'duration': 75}, 
            {'title':'No Time To Die', 'year':2021}, 
            {'title':'Back To The Future', 'year': 1985}, 
            {'title':'No Time To Die 3', 'year':2021}, 
            {'title':'No Time To Die 4', 'year':2021}, 
            ]
    return render(request, 'movieweb/index.html', {'movies': movies})

def detail(request, movie_id):
    return render(request, 'movieweb/movie.html', {'movie_id': movie_id})

def star(request):
    stars = [
            {'name': 'Michael J. Fox', 'birthdate': date(1961,6,9)},
            {'name': 'Christopher Lloyd', 'birthdate': date(1938,10,22)},
            ]
    return render(request, 'movieweb/star.html', {'stars':stars})

def by_year(request, year):
    return HttpResponse(f"Movies from year: {year}")

def by_title(request, title):
    return HttpResponse(f"Movies with title: {title}")

#def by_genre(request, genre):
#    return HttpResponse(f"Movies with genre: {genre}")