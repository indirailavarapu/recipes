from django.urls import path
from .views import *

app_name='nonveg'

urlpatterns=[
    path('chicken/',chicken,name='chicken'),
    path('seafood/',seafood,name='seafood'),
    path('starters/',starters,name='starters'),
    path('meat/',meat,name='meat'),
    path('beef/',beef,name='beef'),
    path('pork/',pork,name='pork'),
    path('showChicken/<int:id>',showChicken,name='showChicken'),
    path('showSeafood/<int:id>',showSeafood,name='showSeafood'),
    path('showStarters/<int:id>',showStarters,name='showStarters'),
    path('showMeat/<int:id>',showMeat,name='showMeat'),
    path('showBeef/<int:id>',showBeef,name='showBeef'),
    path('showPork/<int:id>',showPork,name='showPork'),
]