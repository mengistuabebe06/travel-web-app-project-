from django.contrib import admin
from .models import Destination

# Register your models here.

# to display the tables in column wise instead of list object
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id","name","img","desc","price","offer")
    
admin.site.register(Destination,DestinationAdmin)