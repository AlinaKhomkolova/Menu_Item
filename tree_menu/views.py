from django.shortcuts import get_object_or_404, render
from django.views import View

from .models import MenuItem


class DynamicMenuItemView(View):
    """Представление для отображения страницы по динамическому URL меню.
    Получает пункт меню по URL и рендерит страницу с этим пунктом."""

    def get(self, request, slug):
        # Формируем полный путь URL с ведущим и завершающим слешем
        url_path = '/' + slug.strip('/') + '/'

        # Ищем пункт меню с заданным URL, либо возвращаем 404 если не найден
        menu_item = get_object_or_404(MenuItem, url=url_path)

        # Рендерим шаблон, передавая найденный пункт меню
        return render(request, 'tree_menu/base.html', {
            'menu_item': menu_item,
        })
