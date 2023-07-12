from django.contrib import admin
from .models import Telangana, Hyderabad, Warangal


# Register your models here.

class TelanganaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Telangana,TelanganaAdmin)


class HyderabadAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Hyderabad,HyderabadAdmin)

class WarangalAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Warangal,WarangalAdmin)