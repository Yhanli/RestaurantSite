from django.shortcuts import render
from django.forms.models import model_to_dict
# Create your views here.
from .models import MainPage, MenuPictures, GallaryPictures, VisitorRecord
from django.http import HttpResponse


def main_page(request):
    recordVisitor(request)
    activePage = MainPage.objects.get(is_active=True)
    context = {
        'obj': activePage,
        'navbar':'home'
    }
    return render(request, "home-page.html", context)


def menu_page(request):
    recordVisitor(request)
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
    recordVisitor(request)
    activePage = MainPage.objects.get(is_active=True)
    gallery = GallaryPictures.objects.filter(pageId=activePage.id)
    context = {
        'obj': activePage,
        'gallery': gallery,
        'navbar':'gallery'
    }
    return render(request, "gallery.html", context)

def recordVisitor(request):
    visitor = VisitorRecord()
    visitor.ip = request.META.get('REMOTE_ADDR')
    visitor.visitedPage = request.META.get('PATH_INFO')
    visitor.save()