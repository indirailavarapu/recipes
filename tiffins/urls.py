from django.urls import path
from .views import *

app_name='tiffins'

urlpatterns = [
    path('idly/',idly,name='idly'),
    path('dosa/',dosa,name='dosa'),
    path('vada/',vada,name='vada'),
    path('puri/',puri,name='puri'),
    path('chapati/',chapati,name='chapati'),
    path('parota/',parota,name='parota'),
    path('showIdly/<int:id>',showIdly,name='showIdly'),
    path('showDosa/<int:id>',showDosa,name='showDosa'),
    path('showVada/<int:id>',showVada,name='showVada'),
    path('showPuri/<int:id>',showPuri,name='showPuri'),
    path('showChapati/<int:id>',showChapati,name='showChapati'),
    path('showParota/<int:id>',showParota,name='showParota'),
]