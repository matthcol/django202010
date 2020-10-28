from django.urls import include, path
from rest_framework import routers
from .views import StarViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'stars', StarViewSet)
router.register(r'movies', MovieViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]