from django.urls import path
from .views import *

app_name='veg'

urlpatterns=[
    path('soups/',soups,name='soups'),
    path('curries/',curries,name='curries'),
    path('vegbiryani/',vegbiryani,name='vegbiryani'),
    path('fastfood/',fastfood,name='fastfood'),
    path('starters/',starters,name='starters'),
    path('stirfry/',stirfry,name='stirfry'),
    path('quickandeasy/',quickandeasy,name='quickandeasy'),
    path('showSoups/<int:id>',showSoups,name='showSoups'),
    path('showCurries/<int:id>',showCurries,name='showCurries'),
    path('showVegBiryani/<int:id>',showVegBiryani,name='showVegBiryani'),
    path('showFastFood/<int:id>',showFastFood,name='showFastFood'),
    path('showStarters/<int:id>',showStarters,name='showStarters'),
    path('showStirFry/<int:id>',showStirFry,name='showStirFry'),
    path('showQuickAndEasy/<int:id>',showQuickAndEasy,name='showQuickAndEasy'),

]