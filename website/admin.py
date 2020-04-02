from django.contrib import admin

# Register your models here.
from .models import MainPage, MenuPictures, GallaryPictures, VisitorRecord

admin.site.site_header = "Restaurant Admin"
admin.site.site_title = "Restaurant Admin Portal"
admin.site.index_title = "Welcome to Restaurant Portal"


def make_active(modelamin, request, queryset):
    MainPage.objects.all().update(is_active=False)
    queryset.update(is_active=True)


make_active.short_description = 'Make version active'


class MenuPictureInline(admin.TabularInline):
    model = MenuPictures
    fields = ['picture']


class GallaryPictureInline(admin.TabularInline):
    model = GallaryPictures
    fields = ['picture']


class PageAdmin(admin.ModelAdmin):
    inlines = [MenuPictureInline, GallaryPictureInline, ]
    list_display = ['restaurantEngName',
                    'restaurantSubNameOrTheme',
                    'is_active',
                    ]

    actions = [make_active]


class VisitorRecordAdmin(admin.ModelAdmin):
    list_display = ['ip',
                    'visitorName',
                    'visitedPage',
                    'visitDateTime',
                    ]
    list_display_links = ['ip',
                          'visitorName',
                          'visitedPage',
                          'visitDateTime',
                          ]
    list_filter = ['ip',
                   'visitorName',
                   'visitedPage',
                   'visitDateTime', ]
    search_fields = ['ip',
                     'visitorName',
                     'visitedPage',
                     'visitDateTime', ]


admin.site.register(MainPage, PageAdmin)
admin.site.register(VisitorRecord, VisitorRecordAdmin)
