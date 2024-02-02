from django.http import HttpRequest
from django.shortcuts import render

from .models import Menu


def index(request: HttpRequest):
    return render(request=request, 
                    template_name = 'menu/index.html', 
                    context={
                        'menu_name': request.GET.get('menu_name', 'main_menu'), 
                        })

def menu_list(request: HttpRequest):
    menu_list = Menu.objects.all().values()
    return render(request=request,
                  template_name='menu/menu_list.html',
                  context={'menu_list': menu_list})
