from django.contrib import admin
from .models import Himachal , Manali , Kasol , Shimla , Dalhousie


# Register your models here.

class HimachalPAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class ManaliAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class KasolAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class ShimlaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class DalhousieAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")



admin.site.register(Himachal,HimachalPAdmin)
admin.site.register(Manali,ManaliAdmin)
admin.site.register(Kasol,KasolAdmin)
admin.site.register(Shimla,ShimlaAdmin)
admin.site.register(Dalhousie,DalhousieAdmin)
