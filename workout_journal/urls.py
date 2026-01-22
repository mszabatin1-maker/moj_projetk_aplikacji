from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_detail),
    path('osoby/nazwisko/<str:name>/', views.osoba_name_filter_url),
    path('osoby/nazwisko_param', views.osoba_name_filter_params), #NIE DAJEMY "/" NA KONIEC URI
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
    #ClassBasedViews
    # path("books_vbs/", views.BookListView.as_view(), name="book-list"),
    # path("books_vbs/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    # path('osoby_vbs/', views.OsobaListAPIView.as_view()),
    # path('osoby_vbs/<int:pk>/', views.OsobaDetailAPIView.as_view()),
    # path('osoby_vbs/nazwisko/<str:name>/', views.OsobaSearchAPIView.as_view()),
    # path('osoby_vbs/nazwisko', views.OsobaNameFilterView.as_view()),
    # path('stanowiska_vbs/', views.StanowiskoListAPIView.as_view()),
    # path('stanowiska_vbs/<int:pk>/', views.StanowiskoDetailAPIView.as_view()),
]