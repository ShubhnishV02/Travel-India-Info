from django.contrib import admin
from .models import TamilNadu, Rameshwaram, Yercaud, Kodaikanal, Ooty, Chennai


# Register your models here.

class TamilNaduAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(TamilNadu,TamilNaduAdmin)

class RameshwaramAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Rameshwaram,RameshwaramAdmin)

class YercaudAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Yercaud,YercaudAdmin)

class KodaikanalAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kodaikanal,KodaikanalAdmin)

class OotyAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Ooty,OotyAdmin)

class ChennaiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Chennai,ChennaiAdmin)
