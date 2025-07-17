from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50 , default='nadare')
    meli_code = models.CharField(max_length=10, default=1111111111)
    image = models.ImageField(upload_to='profile/profile_pics',null=True ,blank=True)
    full_name = models.CharField(max_length=50 ,null=True ,blank=True)
    address = models.CharField(max_length=50 , null=True ,blank=True)
    city = models.CharField(max_length=50 , null=True ,blank=True)

    class Meta:
        # dar admin panel in modelo b do shekle mofrad v jam seda zade mishe v ma baid braye shakhsi sazi behesh bgim k mofrd v jame on chi jori bashe
        verbose_name = "  حساب کاربری"
        verbose_name_plural = "حساب های کاربری"

    def __str__(self):
        return f'{self.user.username} , {self.full_name}'
