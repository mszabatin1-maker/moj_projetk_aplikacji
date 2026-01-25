from django.urls import path
from . import views

urlpatterns = [
    path('trener/', views.trener_list),
]