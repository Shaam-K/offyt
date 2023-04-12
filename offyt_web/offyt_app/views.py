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
        search = request.GET['id']


        status = []


        playlist = Playlist(f'https://www.youtube.com/playlist?list={search}')


        directory = playlist.title


        for links in playlist.video_urls:
            playlist_links.append(links)


        exception_count = 0

        for item in playlist_links:

            try:
                item_yt = YouTube(item)

                video_details = {
                    'author': item_yt.author,
                    'title': item_yt.title,
                    'thumb_url': item_yt.thumbnail_url,
                    'link': item,
                }


                playlist_video_info.append(video_details)

            except:
                exception_count += 1
                pass

        generated_links = len(playlist_links) - exception_count


        video_status = []

        playlist_schema = {
            'playlist_name ': str(directory),
            'exception_check': exception_count,
            'total_generated': generated_links
        }

        video_status.append(playlist_schema)

        print(video_status)
            

    context = {'playlist_details': playlist_video_info, 'generated_videos': video_status}
    
    return render(request, 'base.html', context)