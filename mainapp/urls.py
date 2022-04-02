
from django.urls import path
from . import views


urlpatterns = [
    path('', views.test_view, name='home_page'),
    path('raskidki/<slug:map_name>/', views.detail_view_maps_and_grenads, name='detail_grenads'), # <str:place_name>/
    path('raskidki/<slug:map_name>/<slug:place>/', views.place_detail_view, name='place_detail'),
]