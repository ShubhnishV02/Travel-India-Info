from django.db import models

# Create your models here.

class Guide_Booking(models.Model):

    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    
    RADIO_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    ]

    Gender_identity = models.CharField(max_length=10 , choices= RADIO_CHOICES, default='male',  null=True)
    Email = models.EmailField(blank=False, null=False)
    Phone = models.CharField(max_length=20,)
    Address1 = models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200)
    Country = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Guide_Place = models.CharField(max_length=50)
    Guide_Language = models.CharField(max_length=60)
    Availability_Date = models.DateField()

    










    
