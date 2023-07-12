from django.contrib import admin
from .models import Meghalaya, Shillong, Cherrapunji, Williamnagar


# Register your models here.

class MeghalayaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Meghalaya,MeghalayaAdmin)


class ShillongAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Shillong,ShillongAdmin)

class CherrapunjiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Cherrapunji,CherrapunjiAdmin)

class WilliamnagarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Williamnagar,WilliamnagarAdmin)
