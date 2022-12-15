from django.shortcuts import render, redirect
from .models import Room, Topic
from django.db.models import Q
from .forms import RoomForm
# Create your views here.

# request to response

#action

# rooms = [
#     {'id':1, 'name': 'Lets learn'},
#     {'id':2, 'name': 'Lets le'},
#     {'id':3, 'name': 'No learn'},
#]

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    room_count = rooms.count()

    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics':topics, 'room_count':room_count}

    return render(request, 'ollApp/home.html', context)


def  old_sample(request):
    
    return render(request,'myLearningKit_Ex5.html')

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i ['id'] == int(pk):
    #         room = i
    context = {'room':room}

    return render(request, 'room.html',context)

def createRoom(request):
    form = RoomForm()
    print("hello1")
    if request.method == 'POST':
        print("hello2")

        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            #print("hello")
            return redirect('home')
    context = {'form':form}
    return render(request, 'room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {'obj':room}

    return render(request, 'deleteRoom.html', context)
