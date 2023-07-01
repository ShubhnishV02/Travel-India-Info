from django.contrib import admin
from .models import NewDelhi


# Register your models here.

class NewDelhiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(NewDelhi,NewDelhiAdmin)
