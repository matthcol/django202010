from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
#import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Star, Movie
from .serializers import StarSerializer, MovieSerializer


class StarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticated]


# class MovieViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Movie.objects.all().order_by('-year')
#     serializer_class = MovieSerializer
#     permission_classes = [permissions.IsAuthenticated]
    
    
class MovieViewList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'title']

    
    
    @classmethod
    def get_extra_actions(cls):
        return []

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the movies for
    #     the year as determined by the year portion of the URL.
    #     """
    #     year = self.kwargs['year']
    #     return Movie.objects.filter(year=year)