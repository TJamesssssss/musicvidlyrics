# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:44:30 2020

@author: tjame
"""

# WE WANT TO INPUT AN ARTIST - SONG NAME
# THAT INPUT WILL SEARCH AND PULL THE MUSIC VIDE ON YOUTUBE
# THAT INPUT WILL ALSO SEARCH AND PULL THE LYRICS TO THE SONGimport 

import webbrowser
import requests
from apiclient.discovery import build
from bs4 import BeautifulSoup

#YOUTUBE API KEY
api_key = "AIzaSyCUdrlXAfwh0o81utBdoGEEgydXCjYJH0Q"
#GOOGLE API KEY
gapi_key = "AIzaSyB4Ywdt8rgckomPnqumFabHSvNRrIF0rPU"

song_title = input("What song would you like to listen to? ")
artist_name = input("Who is the artist of that song? ")

def youtube_music():    
    youtube = build('youtube', 'v3', developerKey = api_key)
    req = youtube.search().list(q=f'{song_title} {artist_name}', 
                            part='snippet', 
                            type='video', 
                            maxResults = 1)
    res = req.execute()
    for item in res['items']:
        videoId = (item['id']['videoId'])
    webbrowser.open(f'https://www.youtube.com/watch?v={videoId}')
    
def genius_lyrics():
    genius_artist = artist_name.replace(' ','-')
    genius_song = song_title.replace(' ','-')
    webbrowser.open(f'https://genius.com/{genius_artist}-{genius_song}-lyrics')

youtube_music()
genius_lyrics()















# base_url = "http://api.genius.com"
# headers = {'Authorization': 'Bearer 8eT2FmQ4z6Wzb6_wgxuA31lwm4kpNappA-tzlFcBJbvqkoMRVvR8jiiK9HZ3ZUbn'}
# song_api_path = ''

# def music_lyrics(song_api_path):
#     song_url = base_url + song_api_path    
#     response = requests.get(song_url, headers=headers)
#     json = response.json()
#     print(json)
#     path = json["response"]["song"]["path"]
#     # have to do regular html scraping
#     page_url = "http://genius.com" + path
#     page = requests.get(page_url)
#     html = BeautifulSoup(page.text, "html.parser")
#     # have to remove script tags placed in lyrics
#     [h.extract() for h in html('script')]
#     lyrics = html.find("div", class_="lyrics").get_text()
#     return lyrics

# if __name__ == "__main__":
#     search_url = base_url + "/search"
#     data = {'q': song_title}
#     response = requests.get(search_url, data=data, headers=headers)
#     json = response.json()
#     print(json)
#     song_info = None
#     for hit in json["response"]["hits"]:
#         if hit["result"]["primary_artist"]["name"] == artist_name:
#             song_info = hit
#             break
#     if song_info:
#         song_api_path = song_info["result"]["api_path"]
#         print(music_lyrics(song_api_path))

# youtube_music()
# music_lyrics(song_api_path)

# google = build('google', 'v3', developerKey = gapi_key)

# lsearch = google.search().list(q="{song_choce}")
# test = lsearch.execute()
# print(test)

# webbrowser.open(f"https://www.azlyrics.com/lyrics/foofighters/learntofly.html")

# for item in res['items']:
#     print(item['snippet']['title'])

# music = input("Choose your artist - song!")

# url = "https://www.googleapis.com/youtube/v3/search"


# response = requests.get(url, headers = {"Accept": "application/json"})

# data = response.json()

# print(data)

    
