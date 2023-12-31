# Generated by Django 4.2.2 on 2023-07-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Uttarakhand', '0002_auli_dehradun_nainital_rishikesh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haridwar',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Uttarakhand/images')),
                ('Place_name', models.CharField(max_length=70)),
                ('Desc', models.TextField(default='')),
                ('Best_Time', models.CharField(default='', max_length=100)),
                ('Avoid_Time', models.CharField(default='', max_length=100)),
                ('Ideal_Duration', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='', max_length=50)),
                ('More', models.TextField(default='')),
                ('Pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mussoorie',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image', models.ImageField(default='', upload_to='Uttarakhand/images')),
                ('Place_name', models.CharField(max_length=70)),
                ('Desc', models.TextField(default='')),
                ('Best_Time', models.CharField(default='', max_length=100)),
                ('Avoid_Time', models.CharField(default='', max_length=100)),
                ('Ideal_Duration', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='', max_length=50)),
                ('More', models.TextField(default='')),
                ('Pub_date', models.DateField()),
            ],
        ),
    ]
