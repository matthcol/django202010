from django.db import models
from django.urls import reverse

# Create your models here.
        
class Star(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    birthdate=models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.birthdate}, #{self.id})"
    
    def get_absolute_url(self):
        if self.pk is None:
            return reverse('stars')
        else:
            return reverse('star-detail', kwargs={'star_id': self.pk})
    
    class Meta:
        db_table = 'stars'

class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    year=models.SmallIntegerField()
    duration=models.SmallIntegerField(null=True, blank=True)
    
    # association ManyToOne
    # on_delete: CASCADE, SET_NUL, PROTECT
    director=models.ForeignKey(Star,null=True, blank=True,
                                db_column='id_director',
                             #   related_name="+",
                                related_name="directedMovies",
                                on_delete=models.SET_NULL)    
    
    
    # association ManyToMany
    actors=models.ManyToManyField(Star,
                                # db_table="play2",
                                through='Play',
                                through_fields=("movie","actor"),
                                # related_name="+",
                                 related_name="playedMovies")

    def __str__(self):
        return f"{self.title} ({self.year}, #{self.id})"
    
    def get_absolute_url(self):
        if self.pk is None:
            return reverse('movies')
        else:
            return reverse('movie-detail', kwargs={'movie_id': self.pk})
        
    class Meta:
        db_table = 'movies'
        

class Play(models.Model):
    id=models.AutoField(primary_key=True)
    movie=models.ForeignKey(Movie, db_column='id_movie',
                                  on_delete=models.CASCADE)    
    actor=models.ForeignKey(Star, db_column='id_actor',
                                  on_delete=models.CASCADE)    
    role=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'play3'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


