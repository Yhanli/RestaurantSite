from django.db import models
from django.conf import settings
# Create your models here.


class MainPage(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    logoImg = models.ImageField()
    backgroundImg = models.ImageField()
    backgroundImgTime = models.ImageField()
    textSideImg = models.ImageField()
    restaurantEngName = models.CharField(max_length=100)
    restaurantSubNameOrTheme = models.CharField(max_length=100)
    description = models.TextField()
    facebookLink = models.URLField(blank=True, null=True)
    twitterLink = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    lunchOpenHour = models.TextField(blank=True)
    dinnerOpenHour = models.TextField(blank=True)
    googleMapUrl = models.URLField(blank=True)
    contactNumber = models.CharField(blank=True, max_length=20)
    contactEmail = models.EmailField(blank=True)



