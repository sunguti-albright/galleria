from tabnanny import verbose
from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=100),
    image_description = models.CharField(max_length=200),
    image = models.ImageField(upload_to= 'images/', default='')
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE,default='')
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE,default='')
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, Name=None, category=None):
        self.image_name = Name if Name else self.Name
        self.image_category = category if category else self.image_category 
        self.save()


    def __str__(self):
        return self.image_name

   
class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location_name

