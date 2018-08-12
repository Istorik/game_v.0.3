from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from news.models import News, BaseItems
from news.forms import EntryForm

from news.logic import test_free_space_in_inventory, collection_time_test, test_skill, get_update_miner

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
    # Открыт в первый раз
    # Генератор случайного цветка.
    """
    miner = get_object_or_404(BaseItems, id_item=pk)
    height = randint(3, 21)

    if not collection_time_test(qr_id):
        text = 'Ресурс еще не восстановился'
        return render(request, "news/miner.html", {"miner": miner, "text": text})

    if request.POST:
    # Тест формы
        if test_free_space_in_inventory(1) and test_skill(request.POST):
        # Тест умения and Тест места в инвентаре
            text = 'Ресурс собран {}'.format(qr_id)
            #get_update_miner(qr_id, 2)
            update_qr_code(qr_id)
            collect_loot(id_owner,id_item)
        else:
            text = '''Ресурс испорчен.
            Возможно Вам не хватило навыка или у Вас кончилось место в инвентаре'''
        return render(request, "news/miner.html", {"miner": miner, "text": text})
    else:
        form = EntryForm()
    return render(request, "news/miner.html", {"miner": miner, "form": form, 'heignt': height})
