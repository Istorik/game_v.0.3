from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.postgres.fields import JSONField

#dlerkh работа диспачера с сигналами
from django.db.models.signals import post_save
from django.dispatch import receiver
import os, pyqrcode, uuid


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
        ('cloth','ткань'),
        ('chainmail','кольчуга'),
        ('plate','латы'),
        ('tool','инструменты'),
        ('resource','ресурсы'))

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

class Inventory(models.Model):
    '''
    ====inventory================
    | id_owner | id_item | slot |
    | 37       | 1001    | 9    |
  
    '''

    id_owne = models.IntegerField(default=0)
    id_item = models.CharField(max_length=64)
    slot_list = (
        (8,'8_пояс'),
        (9,'9_сумка')
    )
    slot = models.IntegerField(
        choices=slot_list,
        default=9)
    
    class Meta:
        verbose_name = 'Инвентарь игроков'
        verbose_name_plural = 'Инвентарь игроков'

    def __str__(self):
        return "[{}] {}".format(
            self.id_owner,
            self.id_item,
        )

class BaseQrCode(models.Model):
    '''
    ====inventory===============================
    | id_qrcore   | lastupdate | resourse_type |
    | xxx-xxx-xxx | now()      |               |
  
    '''

    id_qrcore = models.CharField("Id QR code",max_length=64)
    lastupdate = models.DateTimeField(auto_now_add=True)
    resource_type_list = (
        ('herb','трава'),
        ('ore','руда'),
        ('wool','шерсть')
    )
    resource_type = models.CharField(
        choices=resource_type_list,
        default='herb',
        max_length=12)

    class Meta:
        verbose_name = 'база QR кодов'
        verbose_name_plural = 'база QR кодов'

    def __str__(self):
        return "[{}] {}".format(
            self.resource_type,
            self.id_qrcore,
        )

@receiver(post_save, sender = BaseQrCode)
def _create_qrcode(instance, **kwargs):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    instance.id_qrcore = str(uuid.uuid4())
    print(instance)
    img = pyqrcode.create(instance.id_qrcore)
    img.png('{}/qrcode/{}.png'.format(BASE_DIR,instance.id_qrcore),scale=6)
    instance.id_qrcore.save()


def inventar_default():
    return {'bag': {'size': 6, 'inventar': [1,2,3,4,5,6]}}

