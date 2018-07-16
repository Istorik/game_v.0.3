from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

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
    user = models.ForeignKey(User, verbose_name="Автор")
    title = models.CharField("Заголовок", max_length=100)
    text_min = models.TextField("Описание квеста")
    text = models.TextField("Текст квеста")
    created = models.DateTimeField("Время публикации квеста", auto_now_add=True)
    time_to_fade = models.DateTimeField("Время протухания квеста")
    level = models.TextField("Допутимые уровни")

