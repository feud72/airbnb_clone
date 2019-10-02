from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    context_object_name = "rooms"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


class RoomDetailView(DetailView):

    """ RoomDetailView Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/room_search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
