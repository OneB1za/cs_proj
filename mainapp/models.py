from django.db import models

# Create your models here.
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import sys
from io import BytesIO


def get_product_url(obj, viewname):
    return reverse(viewname, kwargs={'map_name': obj.map.slug, 'place': obj.place_on_map.slug, 'title_slug': obj.slug})

# Категори на будущее
class Category(models.Model):
    name = models.CharField(max_length=96, verbose_name='Имя категория')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    # Таблица карт


class MapCsGo(models.Model):
    name = models.CharField(max_length=96, verbose_name='Карта')
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', max_length=128,
                                 on_delete=models.CASCADE)  # blank=True, null=True

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
        return get_product_url2(self, 'place_detail')
        #return reverse('place_detail', kwargs={"place": self.slug})  # place_detail


# название класса сменить на более подходящее
class Content(models.Model):
    # Раскидки

    MIN_RESOLUTION = (450, 300)
    MAX_RESOLUTION = (451, 301)
    MAX_IMAGE_SIZE = 3145728

    EAZY = 'Легкая'
    OKAY = 'Средняя'
    HARD = 'Продвинутая'

    DIFFICULTY_CHOISE_FIELD = [
        (EAZY, 'Легкая'),
        (OKAY, 'Средняя'),
        (HARD, 'Продвинутая'),
    ]

    category = models.ForeignKey(Category, verbose_name='Категория', max_length=128, on_delete=models.CASCADE)
    map = models.ForeignKey(MapCsGo, max_length=128, verbose_name='Карта', on_delete=models.CASCADE)
    place_on_map = models.ForeignKey(Place, verbose_name='Место на карте', on_delete=models.CASCADE,
                                     max_length=128)  # blank=True, null=True
    difficulty = models.CharField(choices=DIFFICULTY_CHOISE_FIELD, verbose_name='Сложность броска', null=True,
                                  blank=True, max_length=12)
    title = models.CharField(max_length=128, verbose_name='Название раскидки')
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение карты', blank=True, null=True)
    video = models.FileField(verbose_name='Видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = 'Раскидки'
        verbose_name = 'Раскидка'

    def get_url(self):
        return get_product_url(self, 'grenade_detail_correct')

    # метод по обрезанию изображения миникарты
    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        new_img = img.convert('RGB')
        resized_new_img = new_img.resize((450, 300), Image.ANTIALIAS)
        filestream = BytesIO()
        resized_new_img.save(filestream, 'JPEG', quality=90)
        filestream.seek(0)
        img_name = '{}.{}'.format(*self.image.name.split('.'))
        self.image = InMemoryUploadedFile(
            filestream, 'ImageField', img_name, 'jpeg/image', sys.getsizeof(filestream), None
        )

        super().save(*args, **kwargs)


# комментарии
class Comments(models.Model):
    email = models.EmailField(max_length=96)
    name = models.CharField(max_length=48, verbose_name='Имя')
    text = models.TextField(max_length=1000, verbose_name='Сообщение')
    parents = models.ForeignKey('self', verbose_name='Родители', on_delete=models.SET_NULL, blank=True, null=True)
    grenade = models.ForeignKey(Content, verbose_name='Раскидка', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.grenade}'

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'


'''
class RatingStart(models.Model):
    value = models.PositiveSmallIntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name_plural = 'Звезды рейтинга'
        verbose_name = 'Звезда рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField(verbose_name='IP address', max_length=15)
    star = models.ForeignKey(RatingStart, on_delete=models.CASCADE, verbose_name='Звезды')
    grenade = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Раскидка')

    def __str__(self):
        return f'{self.star} - {self.grenade}'

    class Meta:
        verbose_name_plural = 'Рейтинги'
        verbose_name = 'Рейтинг'
'''
