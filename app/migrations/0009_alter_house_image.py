# Generated by Django 4.0.3 on 2022-09-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]