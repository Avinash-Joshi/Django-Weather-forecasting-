# Generated by Django 4.1 on 2022-11-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0036_alter_data_conditionvsdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='TempVsDate',
            field=models.ImageField(blank=True, default='/Error.png', upload_to='weather/images'),
        ),
    ]