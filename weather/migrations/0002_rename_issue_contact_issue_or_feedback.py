# Generated by Django 4.1 on 2022-11-16 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Issue',
            new_name='Issue_or_Feedback',
        ),
    ]
