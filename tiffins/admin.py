from django.contrib import admin
from .models import *

# Register your models here.
class IdlyAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class DosaAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class PuriAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class VadaAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class ChapatiAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

class ParotaAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description','video']

admin.site.register(Idly,IdlyAdmin)
admin.site.register(Dosa,DosaAdmin)
admin.site.register(Puri,PuriAdmin)
admin.site.register(Vada,VadaAdmin)
admin.site.register(Chapati,ChapatiAdmin)
admin.site.register(Parota,ParotaAdmin)
