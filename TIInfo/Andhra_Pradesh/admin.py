from django.contrib import admin
from .models import AndhraPradesh


# Register your models here.

class AndhraPradeshAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(AndhraPradesh,AndhraPradeshAdmin)
