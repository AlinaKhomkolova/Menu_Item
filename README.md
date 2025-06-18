# Динамическое меню

Этот проект представляет собой пример реализации **динамического многоуровневого меню**.  
Меню поддерживает вложенные пункты, настраивается через админку и легко интегрируется в любой Django-проект.
---
![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2.3%2B-green.svg)
---

## 📋 Содержание

1. [Как развернуть проект](#как-развернуть-проект)
2. [Доступные страницы](#доступные-страницы)
3. [Загрузка фикстур](#загрузка-фикстур)
4. [Автор](#автор)


---

## Как развернуть проект

### 1. Клонирование репозитория

```bash
git clone git@github.com:AlinaKhomkolova/Menu_Item.git
cd Menu_Item
````

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Создание файла .env

Создайте файл .env на основе .env.sample и укажите необходимые параметры.

### 5. Применение миграций

```bash
python manage.py migrate
```

---

## Загрузка фикстур

```bush
python manage.py loaddata fixtures/fixture_market.json
```

```bush
python manage.py loaddata fixtures/fixture_menu.json
```

### Запуск сервера

```bash
python manage.py runserver
```

---

## Доступные страницы

### 1. Меню интернет-магазина

```
http://127.0.0.1:8000/home_market/
```

### 2. Меню услуги компании

```
http://127.0.0.1:8000/home/
```

---

## Автор

**Alina Khomkolova**

Python backend developer