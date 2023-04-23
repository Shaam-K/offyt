from django.shortcuts import render,redirect

from pytube import Playlist

from pytube import YouTube

import os,music_tag

import requests



playlist_video_info = []


# Create your views here.


def home_view(request):
    
    return render(request, 'base.html', {})



def playlist_view(request):
    if request.method == "GET":
        playlist_links = []

        search = request.GET['id']


        playlist = Playlist(f'https://www.youtube.com/playlist?list={search}')


        for links in playlist.video_urls:
            playlist_links.append(links)


        generated_videos = 0


        while generated_videos < len(playlist_links):

            try:
                item_yt = YouTube(playlist_links[generated_videos])

                video_details = {
                    'author': item_yt.author,
                    'title': item_yt.title,
                    'thumb_url': item_yt.thumbnail_url,
                    'link': playlist_links[generated_videos],
                }


                playlist_video_info.append(video_details)

                generated_videos += 1

            except:
                pass


    context = {'playlist_details': playlist_video_info}
    
    return render(request, 'select.html', context)


def playlist_download(request):

    if request.method == "GET":

        video_download = request.GET.getlist('check_vid')


        videos_downloaded = 0

        path = 'offyt_app/static/audiofiles'


        while videos_downloaded < len(video_download):

            try:
                video_obj = YouTube(video_download[videos_downloaded])


                video_filter = video_obj.streams.filter(only_audio=True, file_extension="webm")
                
                video_filter.first().download(path)


                path_files = os.listdir(path)


                print(path_files)


                video_details = {
                    'author': video_obj.author,
                    'title': video_obj.title,
                    'thumb_url': video_obj.thumbnail_url,
                }



                print(video_details)



                ''' 
                
                audiofile = music_tag.load_file(path_files[videos_downloaded])

                audiofile['title'] = video_details['title']
                audiofile['artist'] = video_details['author']

                audiofile.save()
                
                '''

               

    
                videos_downloaded += 1

            except:
                pass
        
    context = {}

    return render(request, 'download.html', context)
