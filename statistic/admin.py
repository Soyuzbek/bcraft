from django.contrib import admin

from statistic.models import Stat


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    pass
