from django.urls import path
from .views import *

app_name='drinks'

urlpatterns = [
    path('milkshakes/',milkshakes,name='milkshakes'),
    path('smoothies/',smoothies,name='smoothies'),
    path('tea/',tea,name='tea'),
    path('coffee/',coffee,name='coffee'),
    path('juices/',juices,name='juices'),
    path('showMilkshakes/<int:id>',showMilkshakes,name='showMilkshakes'),
    path('showSmoothies/<int:id>',showSmoothies,name='showSmoothies'),
    path('showTea/<int:id>',showTea,name='showTea'),
    path('showCoffee/<int:id>',showCoffee,name='showCoffee'),
    path('showJuices/<int:id>',showJuices,name='showJuices'),
]