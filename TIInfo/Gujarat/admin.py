from django.contrib import admin
from .models import Gujarat, Ahmedabad, Kutch, Vadodara


# Register your models here.

class GujaratAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Gujarat,GujaratAdmin)



class AhmedabadAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Ahmedabad,AhmedabadAdmin)



class KutchAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Kutch,KutchAdmin)


class VadodaraAdmin(admin.ModelAdmin):
    list_display = ("Place_name", "Best_Time", "Avoid_Time", "Ideal_Duration", "Pub_date")

admin.site.register(Vadodara,VadodaraAdmin)

