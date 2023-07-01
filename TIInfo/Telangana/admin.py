from django.contrib import admin
from .models import Telangana


# Register your models here.

class TelanganaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Telangana,TelanganaAdmin)
