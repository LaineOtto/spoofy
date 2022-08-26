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
artist_ids = []
playlist = spotify.playlist_items("2V9ylS1wvL5xVwmmAMPKbM")
for track in playlist.items:
    for artist in track.track.artists:
        artist_ids.append(artist.id)
    #     print(artist.id)
    # print("\n")
# print(artist_ids)

# get list of all genres
genre_list = []
for artist_id in artist_ids:
    current_artist = spotify.artist(artist_id)
    # print(current_artist.genres)
    for genre in current_artist.genres:
        genre_list.append(genre)
genre_list.sort()
# print(genre_list)

# count occurences of each genre
genre_counts = []
for genre in genre_list:
    count = genre_list.count(genre)
    if [genre, count] not in genre_counts:
        genre_counts.append([genre, count])
genre_counts.sort(key=lambda k: k[1], reverse=True)  # sorts list by second item
# print(genre_counts)
for genre in genre_counts:
    print(genre)
    print()
