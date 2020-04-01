from django.shortcuts import render

# Create your views here.
from .models import MainPage


def main_page(request):
    activePage = MainPage.objects.get(is_active=True)

    context = {
        'obj':activePage
    }
    return render(request, "home-page.html", context)