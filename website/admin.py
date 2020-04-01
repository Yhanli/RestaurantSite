from django.contrib import admin

# Register your models here.
from .models import MainPage

admin.site.register(MainPage)

admin.site.site_header = "Restaurant Admin"
admin.site.site_title = "Restaurant Admin Portal"
admin.site.index_title = "Welcome to Restaurant Portal"