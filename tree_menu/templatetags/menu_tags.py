from django import template
from django.db.models import Prefetch

from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    # Одно обращение к БД: получаем все пункты нужного меню сразу с их детьми
    menu = Menu.objects.prefetch_related(
        Prefetch('items', queryset=MenuItem.objects.select_related('parent'))
    ).get(name=menu_name)

    items = list(menu.items.all())
    # Собираем дерево в память
    tree = {}
    for item in items:
        tree.setdefault(item.parent_id, []).append(item)

    # Определяем активный пункт и путь к корню
    active = None
    for item in items:
        if item.get_url() == current_path:
            active = item
            break

    active_ids = set()
    node = active
    while node:
        active_ids.add(node.id)
        node = node.parent

    return {
        'tree': tree,
        'parent': None,
        'active_ids': active_ids,
    }


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
