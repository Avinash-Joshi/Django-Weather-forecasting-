# Generated by Django 4.1 on 2022-11-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_rename_issue_contact_issue_or_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('file', models.FileField(default='', upload_to='weather/static/csv')),
            ],
        ),
    ]
