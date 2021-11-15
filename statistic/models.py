from django.db import models
from django.utils.translation import gettext_lazy as _


class Stat(models.Model):
    date = models.DateField(_('date'))
    views = models.IntegerField(_('views'), null=True)
    clicks = models.IntegerField(_('clicks'), null=True)
    cost = models.DecimalField(_('cost'), max_digits=12, decimal_places=2, null=True)

    class Meta:
        verbose_name = _('statistics')
        verbose_name_plural = _('statistics')
        ordering = '-date',
