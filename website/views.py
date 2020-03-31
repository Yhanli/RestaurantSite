from django.shortcuts import render

# Create your views here.
from .models import MainPage


def main_page(request):

    context = {
        'backgroundImg':'https://cdn.cnn.com/cnnnext/dam/assets/200319114749-lake-wanaka-tree-full-169.jpg'
    }
    return render(request, "home-page.html", context)