import json
import requests

artist = str(input("Enter the Artist name:"))
song = str(input("Enter the song name:"))

def extract_lyrics(artist_value, song_value):
    artist_name = artist_value
    song_name = song_value.lower()
    link = f'https://api.lyrics.ovh/v1/{artist_name}/{song_name}'

    try:
        req = requests.get(link)
        json_data = json.loads(req.content)
        lyrics = json_data['lyrics']
        print("\nLyrics printed :: \n\n")
        print(f'{lyrics}\n')
    
    except:
        print("Error Fetching Lyrics")
    
extract_lyrics(artist, song)