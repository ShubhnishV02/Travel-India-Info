from django.contrib import admin
from .models import WestBengal, Kolkata, Darjeeling, Sundarbans, Siliguri


# Register your models here.

class WestBengalAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(WestBengal,WestBengalAdmin)


class KolkataAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kolkata,KolkataAdmin)

class DarjeelingAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Darjeeling,DarjeelingAdmin)

class SundarbansAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Sundarbans,SundarbansAdmin)

class SiliguriAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Siliguri,SiliguriAdmin)
