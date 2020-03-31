from django.urls import path

from .views import main_page


app_name = 'website'

urlpatterns = [
    path('', main_page, name='home-page')
]