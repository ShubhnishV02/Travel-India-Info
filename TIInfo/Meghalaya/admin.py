from django.contrib import admin
from .models import Meghalaya


# Register your models here.

class MeghalayaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Meghalaya,MeghalayaAdmin)
