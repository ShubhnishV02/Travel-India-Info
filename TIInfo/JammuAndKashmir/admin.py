from django.contrib import admin
from .models import JammuAndKashmir , Gulmarg , Srinagar , Pahalgam , Anantnag

# Register your models here.

class JammuKashmirAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class GulmargAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class SrinagarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class PahalgamAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class AnantnagAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(JammuAndKashmir,JammuKashmirAdmin)
admin.site.register(Gulmarg,GulmargAdmin)
admin.site.register(Srinagar,SrinagarAdmin)
admin.site.register(Pahalgam,PahalgamAdmin)
admin.site.register(Anantnag,AnantnagAdmin)


