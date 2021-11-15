from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters, OrderingFilter

from statistic.models import Stat


class StatFilter(filters.FilterSet):
    from_ = filters.DateFilter('date', 'gte')
    to = filters.DateFilter('date', 'lte')

    o = OrderingFilter(
        fields=(
            ('date', 'date'),
            ('cost', 'cost'),
            ('views', 'views'),
            ('cpc', 'cpc'),
            ('cpm', 'cpm'),
        ),

        field_labels={
            'cpc': _('Average cost of clicks'),
            'cpm': _('Average cost of 1000 views')
        })

    class Meta:
        model = Stat
        fields = 'from_', 'to'
