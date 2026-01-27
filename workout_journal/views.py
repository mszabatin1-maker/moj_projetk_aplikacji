from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trener, Podopieczny, Specjalizacja, Cwiczenie, PlanTreningowy
from .serializers import TrenerSerializer, PodopiecznySerializer, SpecjalizacjaSerializer




from django.http import Http404, HttpResponse
import datetime

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def trenerzy_list_html(request):
    trenerzy = Trener.objects.all()
    return HttpResponse(trenerzy)

def trener_list_html(request):
    trenerzy = Trener.objects.all()
    return render(request, "workout_journal/trener/list.html", {'trenerzy' : trenerzy})

def trener_list_html(request):
    trenerzy = Trener.objects.all()
    return render(
        request,
        "workout_journal/trener/list.html",
        {"trenerzy": trenerzy}
    )

def trener_detail_html(request, id):
    try:
        trener = Trener.objects.get(id=id)
    except Trener.DoesNotExist:
        raise Http404("Obiekt Trener o podanym id nie istnieje")

    return render(
        request,
        "workout_journal/trener/detail.html",
        {"trener": trener}
    )

def trener_create_html(request):
    specjalizacje = Specjalizacja.objects.all()

    if request.method == "GET":
        return render(request, "workout_journal/trener/create.html", {'specjalizacje' : specjalizacje})
    elif request.method == "POST":
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        specjalizacja_id = request.POST.get('specjalizacja')

        if imie and nazwisko and specjalizacja_id:
            try:
                specjalizacja_obj = Specjalizacja.objects.get(id = specjalizacja_id)
            except Specjalizacja.DoesNotExist:
                error = "Wybrana specjalizacja nie istnieje."
                return render(request, "workout_journal/trener/create.html", {'error': error, 'specjalizacje': specjalizacje})
            
            Trener.objects.create(
                imie = imie,
                nazwisko = nazwisko,
                specjalizacja = specjalizacja_obj
            )
            return redirect('trener-list')
        else:
            error = "wszystkie pola są wymagane."
            return render(request, "workout_journal/trener/create.html", {'error': error, 'specjalizacje' : specjalizacje})
        
def trener_detail_html(request, id):
    try:
        trener = Trener.objects.get(id = id)
    except Trener.DoesNotExist:
        raise Http404("Obiekt Trener o podanym id nie istnieje")
    
    if request.method == "GET":
        return render(request, "workout_journal/trener/detail.html",
                      {'trener' : trener})
    if request.method == "POST":
        trener.delete()
        return redirect('trener-list')


def podopieczny_list_html(request):
    podopieczni = Podopieczny.objects.all()
    return HttpResponse(podopieczni)

def podopieczny_list_html(request):
    podopieczni = Podopieczny.objects.all()
    return render(request, "workout_journal/podopieczny/list.html", {'podopieczni' : podopieczni})

def podopieczny_list_html(request):
    podopieczni = Podopieczny.objects.all()
    return render(
        request,
        "workout_journal/podopieczny/list.html",
        {"podopieczni": podopieczni}
    )

def podopieczny_detail_html(request, id):
    try:
        podopieczny = Podopieczny.objects.get(id=id)
    except Podopieczny.DoesNotExist:
        raise Http404("Obiekt Podopieczny o podanym id nie istnieje")

    return render(
        request,
        "workout_journal/podopieczny/detail.html",
        {"podopieczny": podopieczny}
    )

def podopieczny_create_html(request):
    trenerzy = Trener.objects.all()

    if request.method == "GET":
        return render(request, "workout_journal/podopieczny/create.html", {'trenerzy' : trenerzy})
    elif request.method == "POST":
        imie = request.POST.get('imie')
        nazwisko = request.POST.get('nazwisko')
        plec = request.POST.get('plec')
        trener_id = request.POST.get('trener')

        if imie and nazwisko and plec and trener_id:
            try:
                trener_obj = Trener.objects.get(id = trener_id)
            except Trener.DoesNotExist:
                error = "Wybrany trener nie istnieje."
                return render(request, "workout_journal/podopieczny/create.html", {'error': error, 'trenerzy': trenerzy})
            
            Podopieczny.objects.create(
                imie = imie,
                nazwisko = nazwisko,
                plec = plec,
                trener = trener_obj
            )
            return redirect('podopieczny-list')
        else:
            error = "wszystkie pola są wymagane."
            return render(request, "workout_journal/podopieczny/create.html", {'error': error, 'trenerzy' : trenerzy})
        
def cwiczenie_list_html(request):
    cwiczenia = Cwiczenie.objects.all()
    return HttpResponse(cwiczenia)

def cwiczenie_list_html(request):
    cwieczenia = Cwiczenie.objects.all()
    return render(request, "workout_journal/cwiczenie/list.html", {'cwiczenia' : cwieczenia})

def cwiczenie_list_html(request):
    cwiczenia = Cwiczenie.objects.all()
    return render(
        request,
        "workout_journal/cwiczenie/list.html",
        {"cwiczenia": cwiczenia}
    )

def cwiczenie_detail_html(request, id):
    try:
        cwiczenie = Cwiczenie.objects.get(id=id)
    except Cwiczenie.DoesNotExist:
        raise Http404("Obiekt Cwiczenie o podanym id nie istnieje")

    return render(
        request,
        "workout_journal/cwiczenie/detail.html",
        {"cwiczenie": cwiczenie}
    )

def cwiczenie_create_html(request):
    planyTreningowe = PlanTreningowy.objects.all()

    if request.method == "GET":
        return render(request, "workout_journal/cwiczenie/create.html", {'planyTreningowe' : planyTreningowe})
    elif request.method == "POST":
        nazwa = request.POST.get('nazwa')
        opis_cwiczenia = request.POST.get('opis_cwiczenia')
        ilosc_powtorzen = request.POST.get('ilosc_powtorzen')
        ilosc_serii = request.POST.get('ilosc_serii')
        planTreningowy_id = request.POST.get("planTreningowy")
        
        
        if nazwa and planTreningowy_id:
            try:
                planTreningowy_obj = PlanTreningowy.objects.get(id = planTreningowy_id)
            except PlanTreningowy.DoesNotExist:
                error = "Wybrany plan treningowy nie istnieje."
                return render(request, "workout_journal/cwiczenie/create.html", {'error': error, 'planyTreningowe': planyTreningowe})
            
            Cwiczenie.objects.create(
                nazwa = nazwa,
                opis_cwiczenia = opis_cwiczenia,
                ilosc_powtorzen = ilosc_powtorzen,
                ilosc_serii = ilosc_serii,
            )
            return redirect('cwiczenie-list')
        else:
            error = "wszystkie pola są wymagane."
            return render(request, "workout_journal/cwiczenie/create.html", {'error': error, 'planyTreningowe' : planyTreningowe})