from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trener, Podopieczny, Specjalizacja
from .serializers import TrenerSerializer, PodopiecznySerializer, SpecjalizacjaSerializer

@api_view(['GET', "POST"])
def trener_list(request):
    """
    Lista wszystkich obiektów modelu Book.
    """
    if request.method == 'GET':
        books = Trener.objects.all()
        serializer = TrenerSerializer(books, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TrenerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)