from django.contrib import admin

# Register your models here.
from .models import MainPage, MenuPictures, GallaryPictures

admin.site.site_header = "Restaurant Admin"
admin.site.site_title = "Restaurant Admin Portal"
admin.site.index_title = "Welcome to Restaurant Portal"


class MenuPictureInline(admin.TabularInline):
    model = MenuPictures
    fields = ['picture']

class GallaryPictureInline(admin.TabularInline):
    model = GallaryPictures
    fields = ['picture']

class PageAdmin(admin.ModelAdmin):
    inlines = [MenuPictureInline, GallaryPictureInline,]


admin.site.register(MainPage, PageAdmin)
