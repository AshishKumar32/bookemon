# Generated by Django 3.1 on 2020-09-30 06:29

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_pictures'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pictures',
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
