import django.db.models as models
from django.contrib.auth.models import AbstractUser

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class Products(models.Model):
    #ID field is automatically created by Django as primary key
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.product_name
    
class AuthUser(AbstractUser):
    #Inherits all fields from AbstractUser
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
     
     # Disable groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='authuser_set',
        blank=True
    )
    # Disable user permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='authuser_permissions_set',
        blank=True
    )
    first_name = None
    last_name = None
    def __str__(self):
        return self.email