from django.contrib import admin
from .models import UttarPradesh, Agra, Varanasi, Vrindavan, Lucknow, Allahabad, Mathura, Ayodhya, Meerut


# Register your models here.

class UttarPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(UttarPradesh,UttarPradeshAdmin)

class AgraAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Agra,AgraAdmin)

class VaranasiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Varanasi,VaranasiAdmin)

class VrindavanAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Vrindavan,VrindavanAdmin)

class LucknowAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Lucknow,LucknowAdmin)

class AllahabadAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Allahabad,AllahabadAdmin)

class MathuraAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Mathura,MathuraAdmin)

class AyodhyaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Ayodhya,AyodhyaAdmin)

class MeerutAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Meerut,MeerutAdmin)



