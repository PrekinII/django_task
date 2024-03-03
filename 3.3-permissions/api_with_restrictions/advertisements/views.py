from django.contrib.auth.models import User

from django_filters.rest_framework import FilterSet, DateFromToRangeFilter


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

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerReadOnly,)
    # def get_permissions(self):
    #     """Получение прав для действий."""
    #     if self.action in ["create", "update", "partial_update", 'delete']: #, 'delete'
    #         return [IsAuthenticated(), IsOwnerReadOnly()] #IsOwnerReadOnly() , IsAdminOrReadOnly()
    #     # elif self.action in ['delete']:
    #     #     return [IsAdminOrReadOnly(),IsAuthenticatedOrReadOnly]
    #     return []

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer