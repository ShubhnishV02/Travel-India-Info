from django.contrib import admin
from .models import UttarPradesh


# Register your models here.

class UttarPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(UttarPradesh,UttarPradeshAdmin)
