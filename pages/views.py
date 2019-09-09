from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def all_torrents(request):
    return render(request, 'pages/all_torrents.html')

def my_torrents(request):
    return render(request, 'pages/my_torrents.html')

def upload(request):
    return render(request, 'pages/upload.html')