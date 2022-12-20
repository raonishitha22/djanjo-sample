from django.db import models

# Create your models here.
class poll(models.Model):
    name=models.CharField(max_length=120)#max_length is required
    gender=models.CharField(max_length=10)
    vote=models.BooleanField()
    email=models.EmailField()
    contib=models.DecimalField(decimal_places=2,max_digits=100011)
    description=models.TextField(blank=True,null=True)
