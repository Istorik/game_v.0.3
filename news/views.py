from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from news.models import News, Miner
from news.forms import EntryForm

from random import randint


def news_list(request):
    """ Вывод списка всех квестов
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news":news})


def new_single(request, pk):
    """ Вывод выбранного квеста
    """
    new = get_object_or_404(News, id=pk)
    return render(request, "news/new_single.html", {"new": new})


def gerbologi(request, pk):
    """ Вывод данных по цветку
    """
    miner = get_object_or_404(Miner, id=pk)
    return render(request, "news/miner.html", {"miner": miner})


def add(request):
    """ Тестовая функция сбора ресурсов
    """
    if 'POST' == request.method:
        form = EntryForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()

    return render(request, 'news/forms.html', {'form': form})


def miner(request, pk):
    """ Вывод данных по ресурсу
        Сбор ресурса
    """
    if 'POST' == request.method:
        form = EntryForm(request.POST)
        if form.is_valid():
            # Тест данных с формы
                # Тест прошел, добавить цветок в инвентарь
            if form.cleaned_data['height'] == 21//3*2:
                print('Ok')
            # таймаут на цветок для этого User
            return HttpResponseRedirect('/')
    else:
        form = EntryForm()
        miner = get_object_or_404(Miner, id=pk)
        height = randint(3, 21)
    return render(request, "news/miner.html", {"miner": miner, "form":form, 'heignt': height})