from django.contrib import admin
from .models import *

# Register your models here.
class ChickenAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class SeafoodAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class StartersAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class MeatAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class BeefAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class PorkAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Chicken,ChickenAdmin)
admin.site.register(Seafood,SeafoodAdmin)
admin.site.register(Starters,StartersAdmin)
admin.site.register(Meat,MeatAdmin)
admin.site.register(Beef,BeefAdmin)
admin.site.register(Pork,PorkAdmin)