from django.db import models

# Create your models here.

class UttarPradesh(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
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
    

class Agra(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Varanasi(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Vrindavan(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Lucknow(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name


class Allahabad(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name


class Mathura(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Ayodhya(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Meerut(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttar_Pradesh/images", default="")
    Place_name = models.CharField(max_length=70)
    Sub_heading = models.CharField(max_length=300, default="")
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name


