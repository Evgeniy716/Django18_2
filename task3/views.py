from django.shortcuts import render
from django.http import HttpResponse


def game_platform(request):
    return render(request, template_name='third_task/platform.html')

def game(request):
    games = {
        'first': 'Atomic Heart',
        'second': 'Cyberpank',
        'third': 'PayDay2'

    }
    return render(request,'third_task/games.html', context=games)


def cart(request):
    return render(request, 'third_task/cart.html')







