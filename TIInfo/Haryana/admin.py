from django.contrib import admin
from .models import Haryana, Chandigarh


# Register your models here.

class HaryanaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Haryana,HaryanaAdmin)


class ChandigarhAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Chandigarh,ChandigarhAdmin)
