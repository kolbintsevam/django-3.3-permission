
from site import USER_BASE
from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class CreatorInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass

class StatusInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    creator = CreatorInFilter(field_name='creator__id', lookup_expr='in')
    status = StatusInFilter(field_name='status', lookup_expr='in')
    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status']