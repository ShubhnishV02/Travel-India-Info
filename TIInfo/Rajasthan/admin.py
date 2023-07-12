from django.contrib import admin
from .models import Rajasthan, Jaipur, Udaipur, Jaisalmer, Jodhpur


# Register your models here.

class RajasthanAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Rajasthan,RajasthanAdmin)


class JaipurAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Jaipur,JaipurAdmin)

class UdaipurAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Udaipur,UdaipurAdmin)

class JaisalmerAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Jaisalmer,JaisalmerAdmin)

class JodhpurAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Jodhpur,JodhpurAdmin)