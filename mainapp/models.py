from django.db import models


# Create your models here.


class Category(models.Model):
    # Категори на будущее
    name = models.CharField(max_length=96, verbose_name='Имя категория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class MapCsGo(models.Model):
    # Таблица карт
    name = models.CharField(max_length=96, verbose_name='Карта')
    slug = models.SlugField(unique=True)
    #ategory = models.ForeignKey(Category, verbose_name='Категория', max_length=128, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    # Название во мн.ч и ед.ч в админки
    class Meta:
        verbose_name_plural = 'Карты'
        verbose_name = 'Карта'


# название класса сменить на более подходящее
class Content(models.Model):
    # Раскидки

    # переменные места на карте, для поля с чойсами
    MIDDLE = 'MID'
    A_SIDE = 'A'
    B_SIDE = 'B'

    PLACE_CHOICES_DATA = [
        (MIDDLE, 'MIDDLE'),
        (A_SIDE, 'A'),
        (B_SIDE, 'B')
    ]

    category = models.ForeignKey(Category, verbose_name='Категория', max_length=128, on_delete=models.CASCADE)
    map = models.ForeignKey(MapCsGo, max_length=128, verbose_name='Карта', on_delete=models.CASCADE)
    place = models.CharField(choices=PLACE_CHOICES_DATA, max_length=3, verbose_name='Место на карте')
    title = models.CharField(max_length=128, verbose_name='Название раскидки')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    video = models.FileField(verbose_name='Видео')

    def __str__(self):
        return f'{self.title}' # | {self.map} | {self.place}'

    class Meta:
        verbose_name_plural = 'Раскидки'
        verbose_name = 'Раскидка'
