from django.contrib import admin
from .models import *

# Register your models here.
class LatestAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description']

class TrendingAdmin(admin.ModelAdmin):
    list_display=['id','name','ingredients','image','description']

admin.site.register(Latest,LatestAdmin)
admin.site.register(Trending,TrendingAdmin)