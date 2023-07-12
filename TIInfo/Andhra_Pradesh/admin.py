from django.contrib import admin
from .models import AndhraPradesh,ArakuValley, Visakhapatnam, Tirupati, Kurnool, Anantapur


# Register your models here.

class AndhraPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(AndhraPradesh,AndhraPradeshAdmin)


class ArakuValleyAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(ArakuValley,ArakuValleyAdmin)


class VisakhapatnamAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Visakhapatnam,VisakhapatnamAdmin)


class TirupatiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Tirupati,TirupatiAdmin)


class KurnoolAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kurnool,KurnoolAdmin)


class AnantapurAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Anantapur,AnantapurAdmin)
