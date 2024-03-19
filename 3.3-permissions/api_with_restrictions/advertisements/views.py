from django.contrib.auth.models import User

from django_filters.rest_framework import FilterSet, DateFromToRangeFilter
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerReadOnly
from advertisements.serializers import AdvertisementSerializer, UserSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdvertisementFilter
    permission_classes = (IsOwnerReadOnly, IsAuthenticatedOrReadOnly,)

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer