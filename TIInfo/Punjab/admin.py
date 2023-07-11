from django.contrib import admin
from .models import Punjab , Amritsar, Pathankot


# Register your models here.

class PunjabPAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class AmritsarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

class PathankotAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")




admin.site.register(Punjab,PunjabPAdmin)
admin.site.register(Amritsar,AmritsarAdmin)
admin.site.register(Pathankot,PathankotAdmin)
