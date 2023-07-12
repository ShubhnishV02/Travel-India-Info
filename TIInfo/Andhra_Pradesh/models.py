from django.db import models

# Create your models here.

class AndhraPradesh(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    Visits_more_places = models.CharField(max_length=90, default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class ArakuValley(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    state = models.CharField(max_length=70)
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Visakhapatnam(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    state = models.CharField(max_length=70)
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Tirupati(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    state = models.CharField(max_length=70)
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name


class Anantapur(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    state = models.CharField(max_length=70)
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Kurnool(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Andhra_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    state = models.CharField(max_length=70)
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
