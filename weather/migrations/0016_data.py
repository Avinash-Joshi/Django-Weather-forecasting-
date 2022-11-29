# Generated by Django 4.1 on 2022-11-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0015_delete_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('State', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('Today_Temp', models.FloatField(default='')),
                ('TempVsDate', models.ImageField(default='Sorry Image Is Unabailabe', upload_to='weather/images')),
                ('Today_wind', models.FloatField(default='')),
                ('Today_condition', models.CharField(default='', max_length=40)),
                ('ConditionVsDate', models.ImageField(default='Something went wrong', upload_to='weather/images')),
            ],
        ),
    ]
