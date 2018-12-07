from django.db import models
from django.contrib.auth.models import User
from rentedproperties.models import Property
# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    the_property = models.ForeignKey(Property,null=True, related_name="reviews", default=1, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title