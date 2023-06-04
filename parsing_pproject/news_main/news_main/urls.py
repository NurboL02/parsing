from django.urls import path
from parser_app.views import parse_akipress



urlpatterns = [

    path('parse_akipress/', parse_akipress, name='parse_akipress'),
]
