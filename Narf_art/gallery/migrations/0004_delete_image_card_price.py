# Generated by Django 4.0.4 on 2022-05-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_alter_card_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='card',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
