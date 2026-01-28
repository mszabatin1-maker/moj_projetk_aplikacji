from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from .models import Trener, Podopieczny, Specjalizacja, Cwiczenie, PlanTreningowy
from .serializers import TrenerSerializer, PodopiecznySerializer, SpecjalizacjaSerializer


@api_view(['GET', 'POST'])
def trener_list(request):
    if request.method == 'GET':
        trenerzy = Trener.objects.all()
        serializer = TrenerSerializer(trenerzy, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TrenerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def trener_detail(request, pk):
    try:
        trener = Trener.objects.get(pk = pk)
    except Trener.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)    
    
    if request.method == 'GET':
        serializer = TrenerSerializer(trener)
        return Response(serializer.data)
    


    
@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def trener_update_delete(request, pk):

    try:
        trener = Trener.objects.get(pk = pk)
    except Trener.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)    
    
    if request.method == 'PUT':
        serializer = TrenerSerializer(trener, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_404_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        trener.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

@api_view(["GET","POST"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def podopieczny_detail(request, pk):
    try:
        podopieczny = Podopieczny.objects.get(pk=pk)
    except Podopieczny.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = PodopiecznySerializer(podopieczny)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = PodopiecznySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["PUT"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def podopieczny_update(request, pk):
    try:
        podopieczny = Podopieczny.objects.get(pk=pk)
    except Podopieczny.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PodopiecznySerializer(podopieczny, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def podopieczny_delete(request, pk):
    try:
        podopieczny = Podopieczny.objects.get(pk=pk)
    except Podopieczny.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        podopieczny.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET"])
def podopieczny_list(request):
    if request.method == "GET":
        return Response(PodopiecznySerializer(Podopieczny.objects.all(),
                                        many = True).data,
                        status = status.HTTP_200_OK)
    
@api_view(["GET"])
def podopieczny_name_filter_url(request, name):
    if request.method == "GET":
        return Response(PodopiecznySerializer(Podopieczny.objects.filter(nazwisko__icontains = name),
                                        many = True).data,
                        status = status.HTTP_200_OK)

@api_view(["GET"])
def podopieczny_name_filter_params(request):
    if request.method == "GET":
        # Pobranie parametru 'name' z query params
        name = request.query_params.get('name', None)
        if name is not None:
            return Response(PodopiecznySerializer(Podopieczny.objects.filter(nazwisko__icontains = name),
                                            many = True).data,
                            status = status.HTTP_200_OK)
        else:
            return Response({"error": "Parametr 'name' jest wymagany."}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET","POST","DELETE"])
def specjalizacja_detail(request, pk):
    try:
        specjalizacja = Specjalizacja.objects.get(pk=pk)
    except Specjalizacja.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = SpecjalizacjaSerializer(specjalizacja)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = SpecjalizacjaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        specjalizacja.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(["GET"])
def specjalizacja_list(request):
    if request.method == "GET":
        return Response(SpecjalizacjaSerializer(Specjalizacja.objects.all(),
                                        many = True).data,
                        status = status.HTTP_200_OK)
    

from rest_framework.authtoken.models import Token

from functools import wraps

def drf_token_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            request.session['token'] = token.key
            request.session['user_id'] = user.id
            return redirect('podopieczny-list')
        else:
            return render(request, 'workout_journal/login.html', {'error': 'Nieprawidłowe dane'})
    return render(request, 'workout_journal/login.html')

def drf_token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token_key = request.session.get('token')
        if not token_key:
            return redirect('drf-token-login')
        try:
            Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            return redirect('drf-token-login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('podopieczny-list')
        else:
            return render(request, 'workout_journal/login.html', {'error': 'Nieprawidłowe dane'})
    return render(request, 'workout_journal/login.html')

def user_logout(request):
    logout(request)
    return redirect('user-login')

def drf_token_logout(request):
    request.session.flush()
    return redirect('drf-token-login')

@login_required(login_url = 'user-login')
def podopieczny_list_owner(request):
    podopieczni = Podopieczny.objects.filter(wlasciciel = request.user)
    return render(request,
                  'workout_journal/podopieczny/list.html',
                  {'podopieczni' : podopieczni})

@drf_token_required
def trener_specjalizacja(request, pk):
    try:
        specjalizacja = Specjalizacja.objects.get(pk = pk)
    except Specjalizacja.DoesNotExist:
        raise Http404("Obiekt Specjaliazacja o podanym id nie istnieje")
    
    if request.method == "GET":
        trenerzy = Trener.objects.filter(specjalizacja = specjalizacja)
        return render(request,
                "workout_journal/trener/list.html",
                {'trenerzy': trenerzy})




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

@drf_token_required
@login_required(login_url='user-login')
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