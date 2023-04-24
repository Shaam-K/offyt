from django.shortcuts import render,redirect

from pytube import Playlist

from pytube import YouTube

import os,music_tag

import requests

import glob



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

        audio_info = []

        video_download = request.GET.getlist('check_vid')

        video_count = len(video_download)


        videos_downloaded = 0

        audio_path = r'offyt_app\static\audiofiles'

        images_path = r'offyt_app\static\imagefiles'


        while videos_downloaded < video_count:

            try:
                video_obj = YouTube(video_download[videos_downloaded])

                video_details = {
                    'author': video_obj.author,
                    'title': video_obj.title,
                    'thumb_url': video_obj.thumbnail_url,
                }

            
                audio_info.append(video_details)


                video_filter = video_obj.streams.filter(only_audio=True, file_extension="mp4")
                
                video_filter.first().download(audio_path)



                videos_downloaded += 1
            except:
                pass


    
        # adding metadata to audiofiles

        meta_pointer = 0

        os.makedirs(images_path)
        
        # Getting the list of files/directories
        # in the specified path Filtering the 
        # list to exclude the directory names
        files = list(filter(os.path.isfile, glob.glob(audio_path + "/*")))

        files.sort(key=os.path.getctime)
        
        
        print(files)


        print(audio_info)



        for file in files:

            image_title = audio_info[meta_pointer]['title']

            url = audio_info[meta_pointer]['thumb_url']


            image_data = requests.get(url).content
            

            image_file = open(f'{images_path}\{meta_pointer}.jpg', 'wb')

            image_file.write(image_data)

            image_file.close
            audiofile = music_tag.load_file(file)
            audiofile['title'] = image_title
            audiofile['artist'] = audio_info[meta_pointer]['author']
            audiofile.save()

            meta_pointer += 1



    

                        
    context = {}

    return render(request, 'download.html', context)
