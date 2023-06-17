from django.shortcuts import render
from .models import Room

rooms = [{"id": 1, "name": "Python"}, {"id": 2, "name": "JS"}, {"id": 3, "name": "Vue"}]


def home(request):
    rooms = Room.objects.all()
    return render(request, "base/home.html", {"rooms": rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    ctx = {"room": room}
    return render(request, "base/room.html", ctx)
