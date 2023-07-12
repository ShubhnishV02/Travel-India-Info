from django.contrib import admin
from .models import ArunachalPradesh , Tawang, Itanagar


# Register your models here.

class ArunachalPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(ArunachalPradesh,ArunachalPradeshAdmin)


class TawangAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Tawang,TawangAdmin)


class ItanagarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Itanagar,ItanagarAdmin)
