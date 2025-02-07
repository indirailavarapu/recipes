from django.urls import path
from .views import *

app_name='desserts'

urlpatterns = [
    path('cakes/',cakes,name='cakes'),
    path('chocolate/',chocolate,name='chocolate'),
    path('icecream/',icecream,name='icecream'),
    path('fruits/',fruits,name='fruits'),
    path('nuts/',nuts,name='nuts'),
    path('cookies/',cookies,name='cookies'),
    path('showCakes/<int:id>',showCakes,name='showCakes'),
    path('showChocolate/<int:id>',showChocolate,name='showChocolate'),
    path('showIcecream/<int:id>',showIceCream,name='showIcecream'),
    path('showFruits/<int:id>',showFruits,name='showFruits'),
    path('showNuts/<int:id>',showNuts,name='showNuts'),
    path('showCookies/<int:id>',showCookies,name='showCookies'),
]