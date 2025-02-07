from django.urls import path
from .views import *

app_name='snacks'

urlpatterns = [
    path('traditional/',traditional,name='traditional'),
    path('chips/',chips,name='chips'),
    path('fries/',fries,name='fries'),
    path('springrolls/',springrolls,name='springrolls'),
    path('showTraditional/<int:id>',showTraditional,name='showTraditional'),
    path('showChips/<int:id>',showChips,name='showChips'),
    path('showFries/<int:id>',showFries,name='showFries'),
    path('showSpringRolls/<int:id>',showSpringRolls,name='showSpringRolls'),
]