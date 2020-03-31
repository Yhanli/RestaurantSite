from django.db import models
from django.conf import settings
# Create your models here.


class MainPage(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    logoImg = models.ImageField()
    backgroundImg = models.ImageField()
    restaurantEngName = models.CharField(max_length=100)
    restaurantChName = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField()



