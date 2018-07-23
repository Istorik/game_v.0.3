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


def miner(request, pk, qr_id):
    """ Вывод данных по ресурсу
        Сбор ресурса
    # Таймаут
    # Пост
        # Тест умения
            # Есть место в инвентаре
        # Не правильный
    # Открыт в первый раз
    # Генератор случайного цветка.
    """
    time_out_miner = '01.01.1999'
    miner = get_object_or_404(Miner, id=pk)
    height = randint(3, 21)

    if not time_out_miner:
        text = 'Ресурс еще не восстановился'
        return render(request, "news/miner.html", {"miner": miner, "text": text})

    if request.POST:
        # Тест формы
        if int(request.POST['user_height']) == int(request.POST['sys_height'])//3*2:
            # Тест умения
            text = 'Ресурс собран {}'.format(qr_id)
                # Тест места в инвентаре
        else:
            text = 'Ресурс испорчен'
        return render(request, "news/miner.html", {"miner": miner, "text": text})
    else:
        form = EntryForm()
    return render(request, "news/miner.html", {"miner": miner, "form": form, 'heignt': height})