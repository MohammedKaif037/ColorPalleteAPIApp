from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
  path("random/", views.get_random_palette, name="random_palette"),
  path("suggested/", views.get_suggested_palette, name="suggested_palette"),
]
