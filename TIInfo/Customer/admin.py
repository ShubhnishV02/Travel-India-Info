from django.contrib import admin
from Customer.models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_email", "customer_country")

admin.site.register(Feedback, FeedbackAdmin)