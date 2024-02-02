from django.urls import path

from .views import index, menu_list

urlpatterns = [
    path('menu_list/', menu_list, name='menu_list'),
    path('', index, name='index'),
]