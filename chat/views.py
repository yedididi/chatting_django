# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")

# # you can give user_name as input here
# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})

def room(request, room_name):
    user_name = request.GET.get('username', 'Anonymous')
    return render(request, "chat/room.html", {"room_name": room_name, "user_name": user_name})

