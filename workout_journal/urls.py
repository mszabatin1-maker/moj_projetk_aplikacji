from django.urls import path, include
from . import views

urlpatterns = [

    path('token/login/', views.drf_token_login, name='drf-token-login'),
    path('token/logout/', views.drf_token_logout, name='drf-token-logout'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    
    path("podopieczni/", views.podopieczny_list),
    path("html/podopieczni/wlasciciel/", views.podopieczny_list_owner, name = "podopieczny-list-owner"),
    path("podopieczni/<int:pk>/edytuj/", views.podopieczny_update, name = "podopieczny-update-drf"),
    path("podopieczni/<int:pk>/usun/", views.podopieczny_delete, name = "podopieczny-delete-drf"),
    path("podopieczni/nazwisko/<str:name>/", views.podopieczny_name_filter_url),
    path("podopieczni/nazwisko_param", views.podopieczny_name_filter_params),
    path("html/podopieczni/dodaj_django/", views.podopieczny_create_django_form, name="podopieczny-create-django"),


    path("podopieczni/<int:pk>/permisje/", views.podopieczny_view),
    path("podopieczni/<int:pk>/permisje_decorator/", views.podopieczny_view_decorator),

    path("trenerzy/", views.trener_list),
    path("trenerzy/<int:pk>/", views.trener_detail),
    path("trenerzy/update_delete/<int:pk>/", views.trener_update_delete),

    path("specjalizacje/", views.specjalizacja_list),
    path("specjalizacje/<int:pk>/", views.specjalizacja_detail),

    path("welcome/", views.welcome_view),
    path("html/trenerzy/", views.trener_list_html, name = "trener-list"),
    path("html/trenerzy/<int:id>/", views.trener_detail_html, name = "trener-detail"),
    path("html/trenerzy/dodaj/", views.trener_create_html, name = "trener-create"),

    path("html/podopieczni/", views.podopieczny_list_html, name = "podopieczny-list"),
    path("html/podopieczni/<int:id>/", views.podopieczny_detail_html, name = "podopieczny-detail"),
    path("html/podopieczni/dodaj/", views.podopieczny_create_html, name = "podopieczny-create"),

    path("html/cwiczenia/", views.cwiczenie_list_html, name = "cwiczenie-list"),
    path("html/cwiczenia/<int:id>/", views.cwiczenie_detail_html, name = "cwiczenie-detail"),
    path("html/cwiczenia/dodaj/", views.cwiczenie_create_html, name = "cwiczenie-create"),

]