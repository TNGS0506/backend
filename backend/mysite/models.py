from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import os

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(_("Image"),upload_to="shoes/", null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)  
    description = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the object
        if self.image:
            # Get the path to the image file
            image_path = self.image.path
            # Delete the file from storage
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)
        
class ShoeImage(models.Model):
    shoe = models.ForeignKey(Shoe, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to="shoe_images/")
    
    def __str__(self):
        return f"{self.shoe.name} Image"

    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args,**kwargs)
        

class Size(models.Model):
    shoe = models.ForeignKey('Shoe', related_name='sizes', on_delete=models.CASCADE)
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size
    
class User(AbstractUser):
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=254)
    image = models.ImageField(upload_to="user_images/", null=True, blank=True)
    
    # Define groups and permissions directly in the User class
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
    # Provide a custom related_name for user_permissions to avoid clashes
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )

class Feedback(models.Model):
    sender = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True) 