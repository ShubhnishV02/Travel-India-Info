from django.contrib import admin
from .models import Assam


# Register your models here.

class AssamAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Assam,AssamAdmin)
