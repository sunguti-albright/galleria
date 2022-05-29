# Generated by Django 4.0.4 on 2022-05-28 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.category'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.location'),
        ),
    ]
