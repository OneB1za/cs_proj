from django.contrib import admin
from django.forms import (ModelChoiceField,
                          ModelForm)
from django.utils.safestring import mark_safe
from .models import (Category,
                     MapCsGo,
                     Content,
                     Place,
                     Comments,)

'''Админка'''
admin.site.site_header = 'Главная страница'
admin.site.index_title = 'Таблицы для создания записей на сайте'


# категории
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']
    ordering = []


# карты
@admin.register(MapCsGo)
class MapCsGoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']
    ordering = []


# раскидки
class ContentAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style ="color:red; font-size:15px;">При загрузке изображения с разрешением больше'
            ' - {}x{}, оно будет обрезано до {}x{}'.format(
                *Content.MAX_RESOLUTION, *Content.MIN_RESOLUTION))


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # автозаполнение с авто подключением жса
    fields = (
        'category', 'map', 'place_on_map', 'difficulty', 'title', 'slug', 'description', 'image', 'get_html_image',
        'video')  # порядок и список полей которые мы будем заполнять
    readonly_fields = ['get_html_image']
    list_display = ['title', 'map', 'place_on_map', 'category', 'get_html_image']  # отображаемые поля
    list_editable = ['map', 'place_on_map']  # поля с возможностью редактирования
    list_filter = ['map', 'place_on_map', 'difficulty']  # поля по которым будут добавлены фильтры
    list_per_page = 10  # кол-во записей на одной странице
    search_fields = ['title']  # поля по которым будет проходить поиск
    ordering = []  # сортировка(убрана дефолтная чтобы не загружать бд)
    form = ContentAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            # показывает не все категории а фильтрует и оставляет только ту в которую мы создаем
            return ModelChoiceField(Category.objects.filter(slug='raskidki'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # функция для отображения фоток в админки
    def get_html_image(self, object):
        # проверка на существование картинки у конкретной раскидки
        if object.image:
            # mark_safe() указывает какие теги не экранировать
            return mark_safe(f'<img src="{object.image.url}" width=60>')

    get_html_image.short_description = 'Миникарта'  # изменяет имя сверху таблицы с get_html_image на указанное


# место на карте
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 10
    search_fields = ['name']
    ordering = []


# комментарии
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'grenade', 'parents']
    list_per_page = 10
    search_fields = ['name']
    ordering = []


'''@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ()


@admin.register(RatingStart)
class RatingStartAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_per_page = 10
    ordering = []
    search_fields = ('value',)'''
