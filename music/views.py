from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album,Song
from django.http import Http404
# Create your views here.

def index(request):
    all_albums=Album.objects.all()
    # context={
    #     'all_albums': all_albums
    # }
    return render(request,'music/index.html',{'all_albums':all_albums})
    # for a in all_albums:
    #     url='/music/'+str(a.id)+'/'
    #     html+='<a href="'+url + '">'+a.album_title+'</a><br>'
       

def detail(request,album_id):
    all_albums=Album.objects.all()
    context={
        'all_albums': all_albums
    }
    # print(HttpResponse('Album.get(album_id)')
    #  all_albums=Album.objects.all()
    #  html=''
    #  for a in all_albums:
    #      if a.id==albumid:
    #          html+=
    # try:
    #     album=Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")
    album=get_object_or_404(Album,pk=album_id) # replacement of try and except 
    return render(request,'music/detail.html',{'album':album})


def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html',{'album':album,'error_message':"you did not select any song"})
    else:
        selected_song.is_fav=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})


