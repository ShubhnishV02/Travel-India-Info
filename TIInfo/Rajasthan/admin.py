from django.contrib import admin
from .models import Rajasthan


# Register your models here.

class RajasthanAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Rajasthan,RajasthanAdmin)
