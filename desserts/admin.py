from django.contrib import admin
from .models import *

# Register your models here.
class CakesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class ChocolateAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class IceCreamAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class FruitsAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class NutsAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class CookiesAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Cakes,CakesAdmin)
admin.site.register(Chocolate,ChocolateAdmin)
admin.site.register(IceCream,IceCreamAdmin)
admin.site.register(Fruits,FruitsAdmin)
admin.site.register(Nuts,NutsAdmin)
admin.site.register(Cookies,CookiesAdmin)