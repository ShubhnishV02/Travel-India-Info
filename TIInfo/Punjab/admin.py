from django.contrib import admin
from .models import Punjab


# Register your models here.

class PunjabPAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Punjab,PunjabPAdmin)
