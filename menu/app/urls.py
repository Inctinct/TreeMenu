from django.urls import path

from .views import base


urlpatterns = [
    path('home/', base, name='home'),
    path('about/', base, name='about'),
    path('price/', base, name='price'),
    path('contacts/', base, name='contacts'),
    path('delivery/', base, name='delivery'),

]