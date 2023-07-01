from django.contrib import admin
from .models import ArunachalPradesh


# Register your models here.

class ArunachalPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(ArunachalPradesh,ArunachalPradeshAdmin)
