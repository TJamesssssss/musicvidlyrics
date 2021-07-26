# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 21:44:30 2020

@author: tjame
"""

# WE WANT TO INPUT AN ARTIST AND SONG NAME WHEN PROMPTED
# THAT INPUT WILL SEARCH AND PULL THE MUSIC VIDEO ON YOUTUBE
# THAT INPUT WILL ALSO SEARCH AND PULL THE LYRICS TO THE SONG FROM GENIUS WEBSITE

import webbrowser
import requests
from apiclient.discovery import build
from bs4 import BeautifulSoup

#YOUTUBE API KEY
api_key = "api_key"
#GOOGLE API KEY
gapi_key = "gapi_key"

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

    
