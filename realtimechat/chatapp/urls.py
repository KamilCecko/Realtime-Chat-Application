from django.urls import path

from .views import rooms, room

urlpatterns = [
    path('', rooms, name='home'),
    path('<str:slug>/', room)
]
