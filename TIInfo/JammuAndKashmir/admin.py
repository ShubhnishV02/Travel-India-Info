from django.contrib import admin
from .models import JammuAndKashmir , Gulmarg

# Register your models here.

class JammuKashmirAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class GulmargAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")



admin.site.register(JammuAndKashmir,JammuKashmirAdmin)
admin.site.register(Gulmarg,GulmargAdmin)


