# Generated by Django 4.0.3 on 2022-08-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(default='property-2.jpg', null=True, upload_to=''),
        ),
    ]