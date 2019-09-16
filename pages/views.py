from django.shortcuts import render, redirect
from django.contrib import messages, auth
from torrents.models import Torrent

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('all_torrents')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('index')
    else:
        return render(request, 'pages/index.html')

def all_torrents(request):
    torrents = Torrent.objects.all()

    context = {
        'torrents': torrents,
    }

    return render(request, 'pages/all_torrents.html', context)

def my_torrents(request):
    return render(request, 'pages/my_torrents.html')

def upload(request):
    return render(request, 'pages/upload.html')