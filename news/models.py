from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.postgres.fields import JSONField

# Create your models here.

User = get_user_model()


class Category(models.Model):
    """ Класс категории квеста
    """
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class News(models.Model):
    """ #156
        Вообще это класс новостей, но у нас новости будут выполнять роль квестов.
        по этому нам понадобятся:
            дата публикации, что бы можно было выдавать квест по времени.
            Количество доступных заявок.
            Время протухания.
            Класс квеста и ограничение по уровню.
        user: Имя персонажа, кто квест выдал и кому собственно его сдавать.
        created: Время в которое квест появится на доскке объявлений
    """
    user = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category,
        verbose_name="Категории квеста",
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField("Заголовок", max_length=100)
    text_min = models.TextField("Описание квеста")
    text = models.TextField("Текст квеста")
    created = models.DateTimeField("Время публикации квеста", auto_now_add=True)
    time_to_fade = models.DateTimeField("Время протухания квеста")
    level = models.TextField("Допутимые уровни")

    class Meta:
        verbose_name = "Квест"
        verbose_name_plural = "Квесты"

    def __str__(self):
        return self.title


class Category_miner(models.Model):
    """ Класс категории Добываемого ресурса
    """
    title = models.CharField("Название", max_length=50)

    class Meta:
        verbose_name = "Категория ресурса"
        verbose_name_plural = "Категории ресурсов"

    def __str__(self):
        return self.title


class Miner(models.Model):
    """ #152
        Классы добываемых ресурсов
        Изначально сделаем 3 добываемых ресурса с 3 уровнями усложнения
        condition Условие сбора ресурса
        condition_text описание Условие сбора ресурса
        category Категория добываемого ресурса
    """
    name = models.CharField("Имя", max_length=100)
    info = models.TextField("Описание ресурса")
    condition_text = models.TextField("Описание условия сбора ресурса")
    condition = models.TextField("условия сбора ресурса")
    level = models.TextField("Уровень", null=1)

    category = models.ForeignKey(
        Category_miner,
        verbose_name="Категория ресурса",
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = "Ресурс"
        verbose_name_plural = "Ресурсы"

    def __str__(self):
        return self.name

class BaseItems(models.Model):
    '''
    =====base_items======================================================================================
    | id_item | item_name   | item_desc           | options             | type_slot | item_type | level |
    | 101     | шапка ушанка| одевается на голову | arm=1.0             | 1         | cloth     | 1     |
    | 1001    | цветок 1    | ростет на лугу      | craft=16,17         | 10        | resource  | 0     |

    '''
    id_item = models.IntegerField(default=0)
    item_name = models.CharField('Название', max_length=64)
    item_desc = models.TextField('Описание предмета')
    options = models.TextField('характеристики')
    type_slot_list = (
        ('1','1_шлем'),
        ('2','2_торс'),
        ('3','3_левая рука'),
        ('4','4_правая рука'),
        ('5','5_перчатки'),
        ('6','6_Штаны'),
        ('7','7_боты'),
        ('8','8_пояс'),
        ('9','9_сумка'))

    type_slot = models.CharField('номер слота',
        choices=type_slot_list,
        default=1,
        max_length=64)

    item_type_list = (
        ('cloth','cloth'),
        ('chainmail','chainmail'),
        ('plate','plate'),
        ('tool','tool'),
        ('resource','resource'))

    item_type = models.CharField('тип предмета',
        choices=item_type_list,
        default='cloth',
        max_length=32)
    
   
    class Meta:
        verbose_name = 'База Предметов'
        verbose_name_plural = 'База Предметов'

    def __str__(self):
        return "[{}] {}".format(
            self.id_item,
            self.item_name,
        )

def inventar_default():
    return {'bag': {'size': 6, 'inventar': [1,2,3,4,5,6]}}

#class Inventar(models.Model):

#    user = models.ForeignKey(
#        User,
#        verbose_name="Название команды",
#        on_delete=models.CASCADE)

#    date = JSONField(default=inventar_default)

#    def __str__(self):
#        return self.date

