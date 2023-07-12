from django.contrib import admin
from .models import Kerala, Munnar, Kumarakom


# Register your models here.

class KeralaAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kerala,KeralaAdmin)


class MunnarAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Munnar,MunnarAdmin)


class KumarakomAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kumarakom,KumarakomAdmin)
