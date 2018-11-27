from django.db import models

TYPE_CHOICES = [
    ('apartment', 'apartment'),
    ('house', 'house'),
    ('room', 'room')
    ]


GENDER_CHOICES = [
    ('male', 'male'),
    ('female', 'female')
    ]
    
    
# Create your models here.
class Landlord(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    town_or_city = models.CharField(max_length=40, blank=False)
    

class Tenant(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    town_or_city = models.CharField(max_length=40, blank=False)
    

class Property(models.Model):
    type_property = models.CharField(max_length=50,choices=TYPE_CHOICES)
    address = models.CharField(max_length=254, default='')
    landlord = models.ForeignKey(Landlord, null=False,on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, null=False,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
                        