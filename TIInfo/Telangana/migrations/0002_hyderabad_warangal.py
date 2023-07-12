# Generated by Django 4.2.2 on 2023-07-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Telangana', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hyderabad',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Telangana/images')),
                ('Place_name', models.CharField(max_length=70)),
                ('Desc', models.TextField(default='')),
                ('state', models.CharField(max_length=70)),
                ('Best_Time', models.CharField(default='', max_length=100)),
                ('Avoid_Time', models.CharField(default='', max_length=100)),
                ('Ideal_Duration', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='', max_length=50)),
                ('More', models.TextField(default='')),
                ('Pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Warangal',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Telangana/images')),
                ('Place_name', models.CharField(max_length=70)),
                ('Desc', models.TextField(default='')),
                ('state', models.CharField(max_length=70)),
                ('Best_Time', models.CharField(default='', max_length=100)),
                ('Avoid_Time', models.CharField(default='', max_length=100)),
                ('Ideal_Duration', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='', max_length=50)),
                ('More', models.TextField(default='')),
                ('Pub_date', models.DateField()),
            ],
        ),
    ]
