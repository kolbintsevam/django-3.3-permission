from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.filters import AdvertisementFilter

from advertisements.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AdvertisementSerializer

from .models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []