from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song
from django.template import loader
# Create your views here.

def index(request):
    all_albums=Album.objects.all()
    html=''
    for a in all_albums:
        url='/music/'+str(a.id)+'/'
        html+='<a href="'+url + '">'+a.album_title+'</a><br>'
        return HttpResponse(html)

def detail(request,album_id):
    # print(HttpResponse('Album.get(album_id)')
    #  all_albums=Album.objects.all()
    #  html=''
    #  for a in all_albums:
    #      if a.id==albumid:
    #          html+=

     return HttpResponse("<h1> this is album id :"+ str(album_id) +"</h2>")
    