# Generated by Django 3.1.14 on 2023-05-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]