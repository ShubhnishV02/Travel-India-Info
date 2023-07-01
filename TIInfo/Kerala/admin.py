from django.contrib import admin
from .models import Kerala


# Register your models here.

class KeralaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Kerala,KeralaAdmin)
