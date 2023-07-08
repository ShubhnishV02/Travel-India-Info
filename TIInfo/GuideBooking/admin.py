from django.contrib import admin
from .models import Guide_Booking


# Register your models here.

class GuideBookingAdmin(admin.ModelAdmin):
    list_display = ("First_name", "Last_name", "Gender_identity", "Phone", "Country", "State", "City", "Availability_Date")


admin.site.register(Guide_Booking,GuideBookingAdmin)

