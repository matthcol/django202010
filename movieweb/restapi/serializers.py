from ..models import Star, Movie
from rest_framework import serializers


class StarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Star
        fields = ['name', 'birthdate']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'year', 'duration', 'director', 'actors']

