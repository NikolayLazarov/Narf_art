# Generated by Django 4.0.4 on 2022-05-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='photo',
            field=models.ImageField(default=False, upload_to='uploads/'),
        ),
    ]