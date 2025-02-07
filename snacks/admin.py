from django.contrib import admin
from .models import *

# Register your models here.
class TraditionalAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class ChipsAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class FriesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class SpringRollsAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Traditional,TraditionalAdmin)
admin.site.register(Chips,ChipsAdmin)
admin.site.register(Fries,FriesAdmin)
admin.site.register(SpringRolls,SpringRollsAdmin)