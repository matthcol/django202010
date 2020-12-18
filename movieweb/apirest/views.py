from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from ..models import Movie, Star
from .serializers import MovieSerializer, StarSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('year')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filterset_fields = ['year', 'title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['year', 'title', 'director__name']


class StarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stars to be viewed or edited.
    """
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticated]



