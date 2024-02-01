from django import template
from django.utils.datastructures import MultiValueDictKeyError

from menu.models import MenuItem


register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Returns dict with actual MenuItems for current item to template draw_menu.html
    """

    items = MenuItem.objects.filter(menu__title__istartswith=menu_name)
    item_values = items.values()
    start_items = [item for item in item_values.filter(parent=None)]

    try:
        selected_item = items.get(id=context['request'].GET.get('item'))
    except MultiValueDictKeyError:
        pass
    except MenuItem.DoesNotExist:
        pass
    else:
        superior_items_ids = get_superior_items_ids(selected_item)
        for parent in start_items:
            if parent['id'] in superior_items_ids:
                parent['child_items'] = get_child_items(
                    parent['id'], superior_items_ids, item_values
                )
    result = {'items': start_items}

    result['menu'] = menu_name
    return result


def get_superior_items_ids(parent):
    """
    Returns set with all superior item ids
    """
    superior_ids = set()
    while parent:
        superior_ids.add(parent.id)
        parent = parent.parent
    return superior_ids


def get_child_items(parent_id, superior_items_ids, item_values):
    """
    Returns list items for current parent items and its child elements
    """
    current_parent_child_list = [
        item for item in item_values.filter(parent_id=parent_id)
    ]
    for child in current_parent_child_list:
        if child['id'] in superior_items_ids:
            child['child_items'] = get_child_items(
                item_values, child['id'], superior_items_ids
            )
    return current_parent_child_list
