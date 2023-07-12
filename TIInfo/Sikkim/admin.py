from django.contrib import admin
from .models import Sikkim, Gangtok, WestSikkim, NorthSikkim


# Register your models here.

class SikkimAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Sikkim,SikkimAdmin)

class GangtokAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Gangtok,GangtokAdmin)

class WestSikkimAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(WestSikkim,WestSikkimAdmin)

class NorthSikkimAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(NorthSikkim,NorthSikkimAdmin)
