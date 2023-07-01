from django.contrib import admin
from .models import Karnataka


# Register your models here.

class KarnatakaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Karnataka,KarnatakaAdmin)
