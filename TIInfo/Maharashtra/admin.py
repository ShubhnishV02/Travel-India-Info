from django.contrib import admin
from .models import Maharashtra, Mahabaleshwar, Mumbai


# Register your models here.

class MaharashtraAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Maharashtra,MaharashtraAdmin)


class MahabaleshwarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Mahabaleshwar,MahabaleshwarAdmin)


class MumbaiAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Mumbai,MumbaiAdmin)
