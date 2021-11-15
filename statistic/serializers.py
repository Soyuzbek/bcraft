from django.utils.translation import gettext_lazy as _
from rest_framework import serializers as srz

from statistic.models import Stat


class StatSerializer(srz.ModelSerializer):
    cpc = srz.DecimalField(12, 2, read_only=True, label=_('Average cost of clicks'))
    cpm = srz.DecimalField(15, 2, read_only=True, label=_('Average cost of 1000 views'))

    class Meta:
        model = Stat
        fields = 'date', 'views', 'clicks', 'cost', 'cpc', 'cpm'
        extra_kwargs = {
            'date': {'format': '%Y-%m-%d', 'input_formats': ['%Y-%m-%d']},
        }
