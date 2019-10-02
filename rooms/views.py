from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    context_object_name = "rooms"
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/room_detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
