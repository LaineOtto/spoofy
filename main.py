import os

# library for reading enviroment variables from .env file
from dotenv import load_dotenv

# spotify api library
import tekore as tk

# load enviroment variables
load_dotenv()
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")

# request app token for spotify api access
app_token = tk.request_client_token(client_id, client_secret)

# create spotify api object
spotify = tk.Spotify(app_token)

# get list of artists
artist_list = []
playlist = spotify.playlist_items("2V9ylS1wvL5xVwmmAMPKbM")
for track in playlist.items:
    for artist in track.track.artists:
        artist_list.append(artist.id)
    #     print(artist.id)
    # print("\n")
print(artist_list)
