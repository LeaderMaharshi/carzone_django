# Generated by Django 4.2 on 2023-04-10 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo',
            field=models.ImageField(upload_to='photos/cars'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_1',
            field=models.ImageField(upload_to='photos/cars'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_2',
            field=models.ImageField(upload_to='photos/cars'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_3',
            field=models.ImageField(upload_to='photos/cars'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(upload_to='photos/cars'),
        ),
    ]
