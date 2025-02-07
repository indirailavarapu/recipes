from django.contrib import admin
from .models import *

# Register your models here.
class MilkshakesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class SmoothiesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class TeaAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class CoffeeAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class JuicesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Milkshakes,MilkshakesAdmin)
admin.site.register(Smoothies,SmoothiesAdmin)
admin.site.register(Tea,TeaAdmin)
admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(Juices,JuicesAdmin)