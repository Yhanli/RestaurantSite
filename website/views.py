from django.shortcuts import render
from django.forms.models import model_to_dict
# Create your views here.
from .models import MainPage, MenuPictures, GallaryPictures, VisitorRecord
from django.http import HttpResponse


def main_page(request):
    try:
        recordVisitor(request)
        activePage = MainPage.objects.get(is_active=True)
        context = {
            'obj': activePage,
            'navbar': 'home'
        }
        return render(request, "home-page.html", context)
    except:
        return HttpResponse('<h1> No active MainPage, add or change object in MainPage')


def menu_page(request):
    recordVisitor(request)
    activePage = MainPage.objects.get(is_active=True)
    menu = MenuPictures.objects.filter(pageId=activePage.id)
    context = {
        'obj': activePage,
        'menu': menu,
        'navbar': 'menu'
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
        'navbar': 'gallery'
    }
    return render(request, "gallery.html", context)


def recordVisitor(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    visitor = VisitorRecord()
    visitor.ip = ip
    visitor.visitedPage = request.META.get('PATH_INFO')
    if request.META.get("USER"):
        visitor.visitorName = request.META.get("USER")


    visitor.save()
