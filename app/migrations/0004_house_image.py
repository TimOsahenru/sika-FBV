# Generated by Django 4.0.3 on 2022-08-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_area_houseimage_housetype_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]