from django.urls import path
from . import views

urlpatterns = [

    path('', views.home_page_view, name='home_page'),  # Главная страница
    path('raskidki/<slug:map_name>/', views.places_on_the_map_view, name='detail_grenads'),
    # Место раскидки на карте
    path('raskidki/<slug:map_name>/<slug:place>/', views.grenades_list_view, name='place_detail'),  # Список раскидок
    path('raskidki/<slug:map_name>/<slug:place>/<slug:title_slug>/', views.grenade_detail_view,
         name='grenade_detail_correct'),  # Конкретная раскидка
    path('about/', views.about_us_view, name='about_us'),  # Страница о нас
    path('contacts/', views.ContactFormView.as_view(), name='contacts'),  # Форма обратной связи(пока не доделал)
    path('comments/<int:id>/', views.AddCommentsView.as_view(), name='add_comments'),  # Комментарии
    # '''path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),'''  # Добавление рейтинга

]
