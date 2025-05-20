from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    meli_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='profile/profile_pics',null=True ,blank=True)


    def __str__(self):
        return self.user.username
