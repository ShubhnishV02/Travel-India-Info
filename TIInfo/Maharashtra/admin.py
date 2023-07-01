from django.contrib import admin
from .models import Maharashtra


# Register your models here.

class MaharashtraAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")


admin.site.register(Maharashtra,MaharashtraAdmin)
