from django.shortcuts import render
import random


def index(request):  # Головна сторінка
    data = {
        'title': 'Головна сторінка',
        'values': ['Some', 'Hello', random.randint(1, 100)],
        'obj': {
            'car': 'BMW',
            'age': 18
        },
    }
    return render(request, 'main/index.html', data)


def tiles(request):
    return render(request, 'main/tiles.html', {'title': 'Плитки'})


def randomint(request):
    data = {
        'title': 'Рандомне число',
        'randint': random.randint(1, 10),
    }
    return render(request, 'main/randint.html', data)


def about(request):
    return render(request, 'main/about.html', {'title': 'Learning Log'})
