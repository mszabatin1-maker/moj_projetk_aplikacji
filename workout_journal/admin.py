from django.contrib import admin

from .models import Podopieczny, Stanowisko, Trener, PlanTreningowy, Cwiczenie



class TrenerAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'stanowisko']
    list_filter = ["stanowisko", "data_dodania"]


class StanowiskoAdmin(admin.ModelAdmin):
    list_filter = ["nazwa"]


admin.site.register(Podopieczny)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Stanowisko , StanowiskoAdmin)
admin.site.register(PlanTreningowy)
admin.site.register(Cwiczenie)