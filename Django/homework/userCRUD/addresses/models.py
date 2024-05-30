from django.db import models
from accounts.models import User

# Create your models here.
class Addresses(models.Model):
    user = models.ForeignKey(User, related_name='addresses',on_delete=models.CASCADE)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self) :
        return f"{self.street}, {self.city}, {self.state}, {self.postal_code},{self.country}"