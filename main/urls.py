from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('',home,name='home'),
    path('veg/',veg,name='veg'),
    path('nonveg/',nonveg,name='nonveg'),
    path('desserts/',desserts,name='desserts'),
    path('snacks/',snacks,name='snacks'),
    path('drinks/',drinks,name='drinks'),
    path('tiffins/',tiffins,name='tiffins'),
    path('calories/',calories,name='calories'),
    path('showLatest/<int:id>',showLatest,name='showLatest'),
    path('showTrending/<int:id>',showTrending,name='showTrending'),
     path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

]