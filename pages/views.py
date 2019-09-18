from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from torrents.models import Torrent
from django.contrib.auth.models import User

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfuly logged in!")
            return redirect('all_torrents')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('index')
    else:
        return render(request, 'pages/index.html')

def all_torrents(request):
    torrents = Torrent.objects.order_by('-date_added')

    context = {
        'torrents': torrents,
    }

    return render(request, 'pages/all_torrents.html', context)

def my_torrents(request):
    torrents = Torrent.objects.filter(added_by=request.user.id)

    context = {
        'torrents': torrents,
    }

    return render(request, 'pages/my_torrents.html', context)

def torrent(request, torrent_id):
    torrent = get_object_or_404(Torrent, pk=torrent_id)

    if request.method == 'POST':
        torrent.delete()
        messages.success(request, 'Torrent successfuly deleted!')
        return redirect('all_torrents')
    else:
        context = {
        'torrent': torrent
        }

        return render(request, 'pages/torrent.html', context)

def upload(request):
    if request.method == 'POST':
        title = request.POST['torrentTitle']
        link = request.POST['torrentLink']
        primary_subtitle = request.POST['primary_subtitle']
        secondary_subtitle = request.POST['secondary_subtitle']


        if Torrent.objects.filter(title=title).exists():
            messages.error(request, "Torrent already exists!")
            return redirect('upload')
        else:
            torrent = Torrent(title=title,
                            link=link,
                            primary_subtitle=primary_subtitle,
                            secondary_subtitle=secondary_subtitle,
                            added_by=request.user
            )
            torrent.save()
            messages.success(request, "Torrent successfuly uploaded!")
            return redirect('all_torrents')
    else:
        return render(request, 'pages/upload.html')

def search(request):
    if request.method == 'POST':
        name = request.POST['torrentName']
        torrents = Torrent.objects.filter(title__icontains = name)

        context = {
            'torrents': torrents,
        }

        return render(request, 'pages/search.html', context)
    else:
        return render(request, 'pages/all_torrents.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfuly logged out!")
        return redirect('index')