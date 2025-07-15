from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50 , null=True ,blank=True)
    meli_code = models.CharField(max_length=10, null=True ,blank=True)
    image = models.ImageField(upload_to='profile/profile_pics',null=True ,blank=True)
    full_name = models.CharField(max_length=50 ,null=True ,blank=True)
    address = models.CharField(max_length=50 , null=True ,blank=True)
    city = models.CharField(max_length=50 , null=True ,blank=True)



    def __str__(self):
        return f'{self.user.username} , {self.full_name}'
