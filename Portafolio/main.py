import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser

client_id = '5c7c480b06344a77abc6e9ea82eb1004'
client_secret = '4a5beb1502514dfa97a43ad9d4a9594c'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

genre = input("Ingresa el genero de musica que quieras escuchar:")

results = sp.search(q='genre:' + str(genre), type='track')
items = results['tracks']['items']
if len(items) > 0:
    track = random.choice(items)
    webbrowser.open("https://open.spotify.com/search/" + track['name'], track['artists'][0]['name'])
    print("Te romendamos esta cancion:" + track['name'], track['artists'][0]['name'])