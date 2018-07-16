from django.db import models
from django.contrib.auth import get_user_model

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
