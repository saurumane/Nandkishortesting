from django.db import models

# Create your models here.
class UserModel(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20)
    usercity=models.CharField(max_length=15)
    useremail=models.EmailField()
    userphone=models.CharField(max_length=13)