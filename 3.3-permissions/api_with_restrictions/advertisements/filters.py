from django_filters.rest_framework import DateFromToRangeFilter, FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']
