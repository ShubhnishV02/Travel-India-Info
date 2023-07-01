from django.contrib import admin
from .models import Gujarat


# Register your models here.

class GujaratAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Gujarat,GujaratAdmin)
