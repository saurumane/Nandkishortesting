from django.db import models

# Create your models here.
class PlansModel(models.Model):
    planid=models.IntegerField(primary_key=True)
    planname=models.CharField(max_length=20)
    plandetails=models.CharField(max_length=30)
    planamount=models.IntegerField()