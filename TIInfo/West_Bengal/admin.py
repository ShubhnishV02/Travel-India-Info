from django.contrib import admin
from .models import WestBengal


# Register your models here.

class WestBengalAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(WestBengal,WestBengalAdmin)
