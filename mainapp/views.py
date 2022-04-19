
from django.shortcuts import (render, redirect)
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import (ContactForm, CommentsForm)
from .models import (Content, MapCsGo, Place)


def home_page_view(request): # Home_page_view
    """Функция представления главной страницы"""

    maps = MapCsGo.objects.all()
    context = {
        'maps': maps,
    }

    return render(request, 'mainapp/base.html', context=context)


def places_on_the_map_view(request, map_name, *args, **kwargs):
    """Функция представления возвращающая страницу
        с местами раскидки на карте"""

    grenades = Content.objects.all().filter(map__slug=map_name)
    places = Place.objects.all()
    context = {
        'grenades': grenades,
        'map_name': map_name,
        'places': places,
    }

    return render(request, 'mainapp/detail_category.html', context=context)


def grenades_list_view(request, map_name: str, place: str):
    """Функция представления возвращающая страницу
        с списком раскидок"""

    grenades = Content.objects.all().filter(place_on_map__slug=place).filter(map__slug=map_name)
    context = {
        'grenades': grenades,
        'map_name': map_name,
        'place': place,
    }
    return render(request, 'mainapp/place_detail.html', context=context)


# обратная связь не готово
def about_us_view(request):
    """Функция не готова, пока заморожена"""
    return render(request, 'mainapp/about_us.html')


class ContactFormView(FormView):
    """Класс представления обратной связи,
        тестово, пока заморожено"""

    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('home_page')

    def form_is_valid(self, form):
        return redirect('home_page')


# комменты
class AddCommentsView(View):
    """Класс представления для добавления
        комментариев к раскидкам"""

    def post(self, request, id):
        form = CommentsForm(request.POST)
        grenade = Content.objects.get(id=id)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parents_id = int(request.POST.get("parent"))
            form.grenade = grenade
            form.save()
        return redirect(grenade.get_url())


'''class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(','[0])
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):

        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                grenade_id=int(request.POST.get('grenade')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
'''


def grenade_detail_view(request, map_name: str, place: str, title_slug: str):
    """Функция представления возвращающая страницу
        с подробной информацией о раскидке"""

    grenade = Content.objects.all().filter(slug=title_slug)
    context = {
        'grenades': grenade,
        'map_name': map_name,
        'place': place,
        'title_slug': title_slug,
    }
    return render(request, 'mainapp/grenade_detail.html', context=context)
