# Generated by Django 4.1 on 2022-11-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0028_alter_data_conditionvsdate_alter_data_tempvsdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='ConditionVsDate',
            field=models.ImageField(default='/media/weather/images/Error.png', null=True, upload_to='weather/images'),
        ),
        migrations.AlterField(
            model_name='data',
            name='TempVsDate',
            field=models.ImageField(default='/media/weather/images/Error.png', null=True, upload_to='weather/images'),
        ),
    ]
