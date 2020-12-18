from rest_framework import serializers
from ..models import Movie, Star


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'duration', 'director', 'actors']
        
class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ['name', 'birthdate']