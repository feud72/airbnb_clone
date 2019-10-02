from django.views.generic import ListView, DetailView
from django.urls import reverse
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
