from django import forms
from .models import Podopieczny, Trener, Specjalizacja

class PodopiecznyForm(forms.ModelForm):
    class Meta:
        model = Podopieczny
        fields = ['imie', 'nazwisko', 'plec', 'trener']

class TrenerForm(forms.ModelForm):
    class Meta:
        model = Trener
        fields = ['imie', 'nazwisko', 'specjalizacja']

class SpecjalizacjaForm(forms.ModelForm):
    class Meta:
        model = Specjalizacja
        fields = ['nazwa', 'opis']