from django.db import models

# Create your models here.

class Uttarakhand(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
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
    

class Rishikesh(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
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
    

class Auli(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
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
    

class Nainital(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
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
    

class Dehradun(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
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
    

class Mussoorie(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name
    

class Haridwar(models.Model):
    place_id = models.AutoField(primary_key=True)
    Image = models.ImageField(upload_to="Uttarakhand/images", default="")
    Place_name = models.CharField(max_length=70)
    Desc = models.TextField(default="")
    Best_Time = models.CharField(max_length=100, default="")
    Avoid_Time = models.CharField(max_length=100, default="")
    Ideal_Duration = models.CharField(max_length=50, default="")
    Category = models.CharField(max_length=50, default="")
    More = models.TextField(default="")
    Pub_date = models.DateField()


    def __str__(self):
        return self.Place_name

