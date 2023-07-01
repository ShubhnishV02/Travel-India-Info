# Generated by Django 4.2.2 on 2023-06-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TamilNadu',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Tamil_Nadu/images')),
                ('Place_name', models.CharField(max_length=70)),
                ('Sub_heading', models.CharField(default='', max_length=300)),
                ('Desc', models.TextField(default='')),
                ('Best_Time', models.CharField(default='', max_length=100)),
                ('Avoid_Time', models.CharField(default='', max_length=100)),
                ('Ideal_Duration', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='', max_length=50)),
                ('Visits_more_places', models.CharField(default='', max_length=90)),
                ('Pub_date', models.DateField()),
            ],
        ),
    ]
