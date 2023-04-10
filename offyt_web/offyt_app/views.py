from django.shortcuts import render,redirect

from pytube import Playlist

from pytube import YouTube

import os,music_tag

import requests



# Create your views here.


def home_view(request):
    return render(request, 'base.html', {})



def playlist_view(request):
    if request.method == "GET":
        playlist_video_info = []
        playlist_links = []
        search = request.GET['url']

        playlist = Playlist(f'https://www.youtube.com/playlist?list={search}')


        directory = playlist.title


        for links in playlist.video_urls:
            playlist_links.append(links)


        if len(playlist_links) == 0:
            print("enter valid playlist")


        for item in playlist_links:

            try:
                item_yt = YouTube(item)

                video_details = {
                    'author': item_yt.author,
                    'title': item_yt.title,
                    'thumb_url': item_yt.thumbnail_url,
                }


                playlist_video_info.append(video_details)

            except:
                pass
            

    context = {'playlist_details': playlist_video_info}
    
    return render(request, 'base.html', context)