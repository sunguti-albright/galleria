# Generated by Django 4.0.4 on 2022-05-29 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_category_location_image_image_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(default='No name', max_length=30),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
        ),
    ]
