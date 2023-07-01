from django.contrib import admin
from .models import Sikkim


# Register your models here.

class SikkimAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Sikkim,SikkimAdmin)
