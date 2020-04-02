from django.shortcuts import render
from django.forms.models import model_to_dict
# Create your views here.
from .models import MainPage, MenuPictures, GallaryPictures
from django.http import HttpResponse


def main_page(request):
    activePage = MainPage.objects.get(is_active=True)

    menu = MenuPictures.objects.filter(pageId=activePage.id)

    print(menu)
    context = {
        'obj': activePage,
        'navbar':'home'
    }
    return render(request, "home-page.html", context)


def menu_page(request):

    activePage = MainPage.objects.get(is_active=True)

    menu = MenuPictures.objects.filter(pageId=activePage.id)
    context = {
        'obj': activePage,
        'menu': menu,
        'navbar':'menu'
    }
    return render(request, "menu.html", context)
    # return HttpResponse('<h1> testing menu</h1>')


def gallary_view(request):

    activePage = MainPage.objects.get(is_active=True)

    gallary = GallaryPictures.objects.filter(pageId=activePage.id)

    context = {
        'obj': activePage,
        'gallary': gallary,
        'navbar':'gallary'
    }
    return render(request, "gallary.html", context)