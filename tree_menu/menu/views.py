from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request=request, 
                    template_name = 'menu/index.html', 
                    context={
                        'menu_name': request.GET.get('menu_name', 'main_menu'), 
                        'item': request.GET.get('item')
                        })
