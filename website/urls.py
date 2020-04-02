from django.urls import path

from .views import main_page, menu_page, gallary_view


app_name = 'website'

urlpatterns = [
    path('', main_page, name='home-page'),
    path('menu/', menu_page, name='menu_page'),
    path('gallary/', gallary_view, name='gallary_page')
]