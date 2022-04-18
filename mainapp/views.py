from django.http import HttpResponse
from django.shortcuts import (render, get_object_or_404, redirect)
from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import (ContactForm, CommentsForm)
from .models import (Content, MapCsGo, Place)


# список карт "/"
def test_view(request):
    maps = MapCsGo.objects.all()

    context = {
        'maps': maps,
    }

    return render(request, 'mainapp/base.html', context=context)


# места на карте
def detail_view_maps_and_grenads(request, map_name, *args, **kwargs):
    grenads_id = get_object_or_404(MapCsGo, slug=map_name)
    grenades = Content.objects.all().filter(map__slug=map_name)

    places = Place.objects.all()
    maps = MapCsGo.objects.all()

    context = {
        'grenades': grenades,
        'map_name': map_name,
        'places': places,
        # 'maps': maps,
    }

    return render(request, 'mainapp/detail_category.html', context=context)


# раскидка
def place_detail_view(request, map_name: str, place: str):
    place_id = get_object_or_404(Place, slug=place)
    grenads_id = get_object_or_404(MapCsGo, slug=map_name)
    grenades = Content.objects.all().filter(place_on_map__slug=place).filter(map__slug=map_name)

    context = {
        'grenades': grenades,
        'map_name': map_name,
        'place': place,
    }
    return render(request, 'mainapp/place_detail.html', context=context)


# обратная связь не готово
def about_us_view(request):
    return render(request, 'mainapp/about_us.html')


# feedback
class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contacts.html'
    success_url = reverse_lazy('home_page')

    def form_is_valid(self, form):
        print(form.cleaned_data)
        return redirect('home_page')


# комменты
class AddCommentsView(View):

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
    #place_id = get_object_or_404(Place, slug=place)
    #grenads_id = get_object_or_404(MapCsGo, slug=map_name)
    #grenade_id = get_object_or_404(Content, slug=title_slug)
    grenade = Content.objects.all().filter(slug=title_slug)
    context = {
        'grenades': grenade,
        'map_name': map_name,
        'place': place,
        'title_slug': title_slug,
    }
    return render(request, 'mainapp/grenade_detail.html', context=context)
