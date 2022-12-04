# Generated by Django 4.1 on 2022-11-20 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0020_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=60)),
                ('Phone', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('Email', models.EmailField(max_length=254)),
                ('Issue_or_Feedback', models.CharField(max_length=1000)),
            ],
        ),
    ]