from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view, name='home_page'),
    path('raskidki/<slug:map_name>/', views.detail_view_maps_and_grenads, name='detail_grenads'),  #

    path('raskidki/<slug:map_name>/<slug:place>/', views.place_detail_view, name='place_detail'),

    path('raskidki/<slug:map_name>/<slug:place>/<slug:title_slug>/', views.grenade_detail_view, name='grenade_detail_correct'),

    path('about/', views.about_us_view, name='about_us'),  # about us
    path('contacts/', views.ContactFormView.as_view(), name='contacts'),  # feedback
    # добавление коммента
    path('comments/<int:id>/', views.AddCommentsView.as_view(), name='add_comments'),
    # добавление рейтинга
    # '''path('add-rating/', views.AddStarRating.as_view(), name='add_rating'),'''

]
