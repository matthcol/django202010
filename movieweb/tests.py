from django.test import TestCase
from .models import Star, Movie

# Create your tests here.

class MovieTest(TestCase):
    
    def test_movie_constructor(self):
        # given
        title = "Mulan"
        year =  2020
        # when
        future_movie = Movie(title=title, year=year)
        # then
        self.assertEqual(future_movie.title, title)
        self.assertEqual(future_movie.year, year)
        self.assertIsNone(future_movie.duration)
        
class MovieDBTest(TestCase):
    
    def setUp(self):
        Movie.objects.create(title="Tenet", year="2020")
        
    def test_movie_default_has_no_director(self):
        movie = Movie.objects.get(title="Tenet")
        print(movie)
        self.assertEqual(movie.title, "Tenet")