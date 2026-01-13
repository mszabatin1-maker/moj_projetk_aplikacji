from django.contrib import admin
from .models import Genre, Author, Book, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'stanowisko']
    list_filter = ["stanowisko", "data_dodania"]

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Osoba, OsobaAdmin)
