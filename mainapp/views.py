from django.shortcuts import render, get_object_or_404
from .models import Content, Category, MapCsGo, Place


# Create your views here.

# TEST VIEW

def test_view(request):
    maps = MapCsGo.objects.all()

    context = {
        'maps': maps,
    }

    return render(request, 'mainapp/base.html', context=context)


def detail_view_maps_and_grenads(request, map_name, ): # place_name
    grenads_id = get_object_or_404(MapCsGo, slug=map_name)
    grenades = Content.objects.all().filter(map__slug=map_name)
    places = Place.objects.all()

    context = {
        'grenades': grenades,
        'places': places,
    }

    return render(request, 'mainapp/detail_category.html', context=context)


def place_detail_view(request, map_name: str, place: str):

    #grenads_id = get_object_or_404(MapCsGo, slug=map_name)

    place_id = get_object_or_404(Place, slug=place)
    grenads_id = get_object_or_404(MapCsGo, slug=map_name)
    grenades = Content.objects.all().filter(place_on_map__slug=place).filter(map__slug=map_name)
    context = {
        'grenades': grenades
    }
    return render(request, 'mainapp/place_detail.html', context=context)

# raskidki vertigo
# A B MID MIDDLE
