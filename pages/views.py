from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages, auth
from torrents.models import Torrent, Genre
from torrents.forms import TorrentForm
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
    genres = Genre.objects.order_by('name')

    paginator = Paginator(torrents, 25)
    page = request.GET.get('page')
    paged_torrents = paginator.get_page(page)

    context = {
        'torrents': paged_torrents,
        'genres': genres,
    }

    return render(request, 'pages/all_torrents.html', context)

def my_torrents(request):
    torrents = Torrent.objects.filter(added_by=request.user.id)
    genres = Genre.objects.order_by('name')

    paginator = Paginator(torrents, 15)
    page = request.GET.get('page')
    paged_torrents = paginator.get_page(page)

    context = {
        'torrents': paged_torrents,
        'genres': genres,
    }

    return render(request, 'pages/my_torrents.html', context)

def torrent(request, torrent_id):
    torrent = get_object_or_404(Torrent, pk=torrent_id)

    if request.method == 'POST':
        torrent.title = request.POST.get("torrentTitle")
        torrent.link = request.POST.get("torrentLink")
        torrent.primary_subtitle = request.POST.get("primarySubtitle")
        torrent.secondary_subtitle = request.POST.get("secondarySubtitle")
        torrent.for_parents = True if request.POST.get('parents') else False
        torrent.save()
        messages.success(request, 'Torrent je uspješno izmjenjen!')
        return redirect('torrent', torrent_id=torrent.id)
    else:
        form = TorrentForm()
        context = {
            'torrent': torrent,
            'form': form,
        }

        return render(request, 'pages/torrent.html', context)

def torrent_delete(request, torrent_id):
    torrent = get_object_or_404(Torrent, pk=torrent_id)

    if request.method == 'POST':
        torrent.delete()
        messages.success(request, 'Torrent successfuly deleted!')
        return redirect('all_torrents')

def upload(request):
    if request.method == 'POST':
        form = TorrentForm(data=request.POST)
        if form.is_valid():
            title = request.POST['torrentTitle']
            year = request.POST['release-year']
            link = request.POST['torrentLink']
            primary_subtitle = request.POST['primary_subtitle']
            secondary_subtitle = request.POST['secondary_subtitle']
            for_parents = True if request.POST.get('parents') else False


            if Torrent.objects.filter(title=title).exists():
                messages.error(request, "Torrent već postoji!")
                return redirect('upload')
            elif year == 'select-year':
                messages.error(request, "Unesite ispravno godinu!")
                return redirect('upload')
            else:
                torrent = Torrent(title=title,
                                year=year,
                                link=link,
                                primary_subtitle=primary_subtitle,
                                secondary_subtitle=secondary_subtitle,
                                for_parents=for_parents,
                                added_by=request.user
                )
                torrent.save()
                for genre_pk in form.cleaned_data['genres']:
                    genre = Genre.objects.get(pk=genre_pk)
                    torrent.genres.add(genre)
                torrent.save
                messages.success(request, "Torrent successfuly uploaded!")
                return redirect('all_torrents')
        else:
            messages.error(request, "You must select a genre!")
            context = {
                'form': form
            }
            return render(request, 'pages/upload.html', context)
        
    else:
        form = TorrentForm()
        context = {
            'form': form,
        }
        return render(request, 'pages/upload.html', context)

def search(request):
    genres = Genre.objects.order_by('name')

    if request.method == 'POST':
        name = request.POST['torrentName']
        genre = request.POST['genre']
        torrents = Torrent.objects.filter(title__icontains=name)
        
        if genre!='all':
            torrents = torrents.filter(genres__id=genre)

        context = {
            'torrents': torrents,
            'genres': genres,
        }

        return render(request, 'pages/search.html', context)
    else:
        return render(request, 'pages/all_torrents.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "Successfuly logged out!")
        return redirect('index')