from django.db import models
from django.urls import reverse

from main.settings import NULLABLE


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Идентификатор меню')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self',
        **NULLABLE,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Родитель'
    )
    title = models.CharField(max_length=200, verbose_name='Название пункта')
    url = models.CharField(max_length=200, blank=False, verbose_name='URL (literal)')
    named_url = models.CharField(max_length=200, **NULLABLE, verbose_name='Named URL')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        ordering = ['order']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункт меню'

    def get_url(self):
        """Метод для получения финального URL"""
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.title
