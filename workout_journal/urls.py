from django.urls import path
from . import views

urlpatterns = [

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