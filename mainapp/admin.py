from django.contrib import admin
from django.forms import ModelChoiceField

from .models import Category, MapCsGo, Content, Place


# admin.site.register()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # авто заполнение слага через поле имени
    list_display = ['name']


@admin.register(MapCsGo)
class MapCsGoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'map', 'place_on_map']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # условие проверки
        if db_field.name == 'category':
            # показывает не все категории а фильтрует и оставляет только ту в которую мы создаем
            return ModelChoiceField(Category.objects.filter(slug='raskidki'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']