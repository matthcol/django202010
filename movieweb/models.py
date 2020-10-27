from django.db import models
from django.urls import reverse

# Create your models here.
        
class Star(models.Model):
    id=models.IntegerField(primary_key=True)
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
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=250)
    year=models.SmallIntegerField()
    duration=models.SmallIntegerField(null=True)
    
    # association ManyToOne
    # on_delete: CASCADE, SET_NUL, PROTECT
    director=models.ForeignKey(Star,null=True,
                                db_column='id_director',
                             #   related_name="+",
                                related_name="directedMovies",
                                on_delete=models.SET_NULL)    
    
    
    # association ManyToMany
    actors=models.ManyToManyField(Star,
                                 db_table="play",
                                # related_name="+",
                                 related_name="playedMovies",
                                 db_column=("id_movie", "id_actor"))

    
    
    def __str__(self):
        return f"{self.title} ({self.year}, #{self.id})"
        
    class Meta:
        db_table = 'movies'