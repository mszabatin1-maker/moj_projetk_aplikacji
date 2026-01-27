from django.db import models
from django.contrib.auth.models import User

# Lista wyboru miesięcy wydania
MONTHS = models.IntegerChoices(
    'Miesiace',
    'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień'
)
    
PLCIE = models.IntegerChoices(
    'Plcie',
    'Kobieta Mezczyzna Inna'
)
    

class Trener(models.Model):
    imie = models.CharField(max_length=50, blank = False, null = False)
    nazwisko = models.CharField(max_length=100, blank = False, null = False)
    data_dodania = models.DateField(auto_now_add = True, editable = False)
    specjalizacja = models.ForeignKey('Specjalizacja', on_delete=models.CASCADE)
    wlasciciel = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, default = 1)
    # plan_treningowy = models.ForeignKey('PlanTreningowy', on_delete=models.CASCADE)
    # cwiczenie = models.ForeignKey('PlanTreningowy',on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Trener: {self.imie} {self.nazwisko}"

class Podopieczny(models.Model):
    PLEC_WYBOR = (
        ("1", "kobieta"),
        ("2", "mezczyzna"),
        ("3", "inna")
    )
    imie = models.CharField(max_length=50, blank = False, null = False)
    nazwisko = models.CharField(max_length=100, blank = False, null = False)
    plec = models.IntegerField(choices=PLCIE.choices, default=PLCIE.Inna)
    trener = models.ForeignKey(Trener, null = True, blank = True, on_delete = models.SET_NULL)
    plan_treningowy = models.ManyToManyField('PlanTreningowy')
    data_dodania = models.DateField(auto_now_add = True, editable = False)

    def __str__(self):
        return f"Podopieczny: {self.imie} {self.nazwisko}"
    
    class Meta: 
        ordering = ['nazwisko']

class Cwiczenie(models.Model):
    nazwa = models.CharField(max_length = 70, blank = False, null = False)
    opis_cwiczenia = models.TextField(blank = True, null = True)
    ilosc_powtorzen = models.IntegerField()
    ilosc_serii = models.IntegerField()
    # dodaj_do_plan_treningowy = models.ManyToManyField('PlanTreningowy')   

    def __str__(self):
        return f"{self.nazwa}"

class PlanTreningowy(models.Model):
    nazwa = models.CharField(max_length = 70, blank = False, null = False)
    cwiczenia = models.ManyToManyField('Cwiczenie')

    def __str__(self):
        return f"{self.nazwa}"


class Specjalizacja(models.Model):
    nazwa = models.CharField(max_length = 70, blank = False, null = False)
    opis = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.nazwa}"

