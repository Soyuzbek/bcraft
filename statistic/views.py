from django.db.models import (
    Case,
    DecimalField,
    F,
    When,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    UpdateModelMixin,
)

from statistic.filters import StatFilter
from statistic.serializers import (
    StatSerializer,
)
from statistic.models import Stat


class StatViewSet(ViewSetMixin,
                  CreateModelMixin,
                  ListModelMixin,
                  UpdateModelMixin,
                  GenericAPIView):
    filter_backends = DjangoFilterBackend,
    filterset_class = StatFilter

    def get_queryset(self):
        qs = Stat.objects.annotate(
            cpc=Case(When(clicks=0, then=0), default=F('cost') / F('clicks'), output_field=DecimalField(12, 2)),
            cpm=Case(When(views=0, then=0), default=F('cost') / F('views') * 1000, output_field=DecimalField(15, 0))
        )
        return qs

    def get_serializer_class(self):
        return StatSerializer

    @action(['DELETE'], False)
    def reset(self, request, *args, **kwargs):
        Stat.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
