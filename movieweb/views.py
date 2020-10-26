from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'movieweb/index.html', {'nbMovies':150})

def detail(request, movie_id):
    render(request, 'movieweb/movie.html', {'movie_id': movie_id})

def by_year(request, year):
    return HttpResponse(f"Movies from year: {year}")

def by_title(request, title):
    return HttpResponse(f"Movies with title: {title}")

#def by_genre(request, genre):
#    return HttpResponse(f"Movies with genre: {genre}")