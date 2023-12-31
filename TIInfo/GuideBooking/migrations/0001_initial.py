# Generated by Django 4.2.2 on 2023-07-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Gender_identity', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=20)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200)),
                ('Country', models.CharField(max_length=20)),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Guide_Place', models.CharField(max_length=50)),
                ('Guide_Language', models.CharField(max_length=60)),
                ('Availability_Date', models.DateField()),
            ],
        ),
    ]
