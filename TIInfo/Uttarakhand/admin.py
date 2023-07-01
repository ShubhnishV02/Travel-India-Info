from django.contrib import admin
from .models import Uttarakhand


# Register your models here.

class UttarakhandAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Uttarakhand,UttarakhandAdmin)
