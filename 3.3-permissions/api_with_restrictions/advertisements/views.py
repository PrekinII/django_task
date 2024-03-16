from django.contrib.auth.models import User

from django_filters.rest_framework import FilterSet, DateFromToRangeFilter
from rest_framework.exceptions import PermissionDenied

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
    filterset_class = AdvertisementFilter
    permission_classes = (IsOwnerReadOnly, IsAuthenticatedOrReadOnly,)

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    #def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update", 'delete']: #, 'delete'
    #         return [IsOwnerReadOnly()]
    #     # elif self.action in ['delete']:
    #     #     return [IsOwnerReadOnly]
    #     return []
    # def get_permissions(self):
    #     if self.action == ["create", "update", "partial_update", 'delete']:
    #         permission_classes = [IsOwnerReadOnly]
    #     else:
    #         permission_classes = [IsAuthenticatedOrReadOnly]
    #     return [permission() for permission in permission_classes]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer