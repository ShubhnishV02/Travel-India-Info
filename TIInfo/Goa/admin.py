from django.contrib import admin
from .models import Goa


# Register your models here.

class GoaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Goa,GoaAdmin)
