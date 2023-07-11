from django.contrib import admin
from .models import Uttarakhand, Rishikesh, Auli, Nainital, Dehradun, Mussoorie, Haridwar


# Register your models here.

class UttarakhandAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Uttarakhand,UttarakhandAdmin)


class RishikeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Rishikesh,RishikeshAdmin)


class AuliAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Auli,AuliAdmin)


class NainitalAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Nainital,NainitalAdmin)


class DehradunAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Dehradun,DehradunAdmin)


class MussoorieAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Mussoorie,MussoorieAdmin)

class HaridwarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Haridwar,HaridwarAdmin)
