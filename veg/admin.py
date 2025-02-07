from django.contrib import admin
from .models import *

# Register your models here.
class SoupsAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class CurriesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class VegBiryaniAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class FastFoodAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class StartersAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class StirFryAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class QuickAndEasyAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Soups,SoupsAdmin)
admin.site.register(Curries,CurriesAdmin)
admin.site.register(VegBiryani,VegBiryaniAdmin)
admin.site.register(FastFood,FastFoodAdmin)
admin.site.register(Starters,StartersAdmin)
admin.site.register(StirFry,StirFryAdmin)
admin.site.register(QuickAndEasy,QuickAndEasyAdmin)