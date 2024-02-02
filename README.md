Решение тестового задания.
(Задание: реализовать древовидное меню через template tag)

В проекте два пользовательских эндпоинта:

  GET / - принимает два query params: menu_name и item - название меню и id выбранного элемента меню. 
          Возвращает html страницу с меню, в котором все родительские элементы от выбранного до самых старших развёрнуты. При этом все остальные элементы остаются свёрнутыми.

  GET /menu_list/ - возвращает html страницу со всеми меню (без элементов, только названия и дата создания).

В проекте реализованы 2 модели: Menu и MenuItem     
Меню и элементы меню возможно добавлять и удалять через стандартную админку Django

Установка:     
/для Windows/
```
git clone https://github.com/leggongum/tree_menu_django.git
cd tree_menu_django
virtualenv venv
cd tree_menu
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
```

/для Linux/
```
git clone https://github.com/leggongum/tree_menu_django.git
cd tree_menu_django
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

/через Docker/
```
git clone https://github.com/leggongum/tree_menu_django.git
cd tree_menu_django
docker build . -t tree_menu
docker run -p 8000:8000 tree_menu
```
