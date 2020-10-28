from ..models import Star, Movie
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StarSerializer, MovieSerializer


class StarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-year')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]