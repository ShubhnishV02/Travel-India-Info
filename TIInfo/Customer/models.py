from django.db import models

# Create your models here.

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=17)
    customer_country = models.CharField(max_length=30, default="")
    customer_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
