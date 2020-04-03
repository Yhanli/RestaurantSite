from django.db import models
from django.conf import settings
# Create your models here.


class MainPage(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    favIconImg = models.ImageField(blank=False, null=False)
    logoImg = models.ImageField(blank=False, null=False)
    backgroundImg = models.ImageField(blank=False, null=False)
    backgroundImgTime = models.ImageField(blank=False, null=False)
    textSideImg = models.ImageField(blank=False, null=False)
    embedInfoFromOtherSite = models.TextField(blank=True)
    restaurantEngName = models.CharField(max_length=100)
    restaurantSubNameOrTheme = models.CharField(max_length=100)
    description = models.TextField(blank=False, null=False)
    facebookLink = models.URLField(blank=True, null=True)
    youtubeLink = models.URLField(blank=True, null=True)
    twitterLink = models.URLField(blank=True, null=True)
    lunchOpenHour = models.TextField(blank=True)
    dinnerOpenHour = models.TextField(blank=True)
    googleMapUrl = models.URLField(blank=True)
    contactNumber = models.CharField(blank=True, max_length=20)
    contactEmail = models.EmailField(blank=True)
    menuImg = None
    galleryImg = None


class MenuPictures(models.Model):
    picture = models.ImageField(upload_to="menu/", blank=True)
    pageId = models.ForeignKey('MainPage', on_delete=models.CASCADE,)

class GallaryPictures(models.Model):
    picture = models.ImageField(upload_to="gallary/", blank=True)
    pageId = models.ForeignKey('MainPage', on_delete=models.CASCADE,)


class VisitorRecord(models.Model):
    ip = models.GenericIPAddressField()
    visitDateTime = models.DateTimeField(auto_now_add=True)
    visitedPage = models.CharField(max_length=100)
    visitorName = models.CharField(max_length=120, blank=True, null=True)