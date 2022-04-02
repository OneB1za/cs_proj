from django.db import models

# Create your models here.
from django.urls import reverse






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
    category = models.ForeignKey(Category, verbose_name='Категория', max_length=128, on_delete=models.CASCADE,
                                 blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    # Название во мн.ч и ед.ч в админки
    class Meta:
        verbose_name_plural = 'Карты'
        verbose_name = 'Карта'

    def get_url(self):
        return reverse('detail_grenads', args=(self.slug,))


# ПОЛОЖЕНИЕ ПЛЕЙС ОПАСНО НОЧЬЮ ДЕЛАЮ ЗАВТРА НИЧЕГО МОГУ НЕ ВСПОМНИТЬ
class Place(models.Model):
    name = models.CharField(max_length=64, verbose_name='Место на карте')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Места на карте'
        verbose_name = 'Место на карте'

    def get_url(self):
        return reverse('place_detail', kwargs={"place": self.slug})  # place_detail




# название класса сменить на более подходящее
class Content(models.Model):
    # Раскидки

    # переменные места на карте, для поля с чойсами
    # MIDDLE = 'MID'
    # A_SIDE = 'A'
    # B_SIDE = 'B'

    # PLACE_CHOICES_DATA = [
    # (MIDDLE, 'MIDDLE'),
    # (A_SIDE, 'A'),
    # (B_SIDE, 'B')
    # ]

    category = models.ForeignKey(Category, verbose_name='Категория', max_length=128, on_delete=models.CASCADE)
    map = models.ForeignKey(MapCsGo, max_length=128, verbose_name='Карта', on_delete=models.CASCADE)
    # place = models.CharField(choices=PLACE_CHOICES_DATA, max_length=3, verbose_name='Место на карте')
    place_on_map = models.ForeignKey(Place, verbose_name='Место на карте', on_delete=models.CASCADE, max_length=128,
                                     blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name='Название раскидки')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение карты', blank=True, null=True)
    video = models.FileField(verbose_name='Видео')

    def __str__(self):
        return f'{self.title}'  # | {self.map} | {self.place}'

    class Meta:
        verbose_name_plural = 'Раскидки'
        verbose_name = 'Раскидка'
