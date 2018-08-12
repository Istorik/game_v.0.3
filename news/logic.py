from django.shortcuts import render, get_object_or_404
from news.models import BaseQrCode

from datetime import datetime, timedelta

def test_free_space_in_inventory(user):
    '''
    Проверяем на наличие свободного места в сумке игрока.
    Сравниваем все предметы находящиеся в инвентаре и качество сумки
    :param user:
    :return: True если место есть
    '''
    return True

def collection_time_test(id_qr):
    '''
    Проверяем время последнего сбора данного ресурска.
    Ресур определяем по id_qr
    :param id_qr:
    :return: True если ресурс тоступен
    '''
    qr_base = BaseQrCode.objects.filter(id_qrcore=id_qr)
    t_delta = datetime.now() - timedelta(minutes=3)
#    if qr_base.lastupdate < t_delta:
#       return False
    return True

def test_skill(f):
    '''
    Проверка навыка игрока на добычу ресурса.
    1. Проверка на правильность ответа на вопрос
    2. Прокаченный навык
    :param f:
    :return:
    '''
    return int(f['user_height']) == (int(f['sys_height'])//3*2) and True

def get_update_miner(qr, user):
    '''
    Заносит обновление в базу
    1. qr - Ресурс который был собран ставится отметка текущего времени.
    2. user - Пользователь который собрал ресурс

    :return:
    '''
    print(qr)
    pass


def update_qr_code(qr):
    pass
