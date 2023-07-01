from django.contrib import admin
from .models import JammuAndKashmir

# Register your models here.

class JammuKashmirAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")



admin.site.register(JammuAndKashmir,JammuKashmirAdmin)


