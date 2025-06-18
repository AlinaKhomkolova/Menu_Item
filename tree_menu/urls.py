from django.urls import path

from tree_menu.apps import TreeMenuConfig
from tree_menu.views import DynamicMenuItemView

app_name = TreeMenuConfig.name

urlpatterns = [
    # Динамическое отображение меню
    path('<path:slug>/', DynamicMenuItemView.as_view(), name='dynamic_menu'),
]
