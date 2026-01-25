from django.contrib import admin

from .models import Podopieczny, Specjalizacja, Trener, PlanTreningowy, Cwiczenie



class TrenerAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'specjalizacja']
    list_filter = ["specjalizacja", "data_dodania"]


class SpecjalizacjaAdmin(admin.ModelAdmin):
    list_filter = ["nazwa"]



admin.site.register(Podopieczny)
admin.site.register(Trener, TrenerAdmin)
admin.site.register(Specjalizacja , SpecjalizacjaAdmin)
admin.site.register(PlanTreningowy)
admin.site.register(Cwiczenie)