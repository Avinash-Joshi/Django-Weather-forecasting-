# Generated by Django 4.1 on 2022-11-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0042_alter_data_conditionvsdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ConditionVsDate',
            field=models.ImageField(blank=True, default='E:/Miniproject/Weatherforecasting/media/weather/images/Error.png', upload_to='weather/images'),
        ),
    ]
