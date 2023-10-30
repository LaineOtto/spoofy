import os

# library for reading enviroment variables from .env file
from dotenv import load_dotenv

# spotify api library
import tekore as tk

def loadEnvironment():
    load_dotenv()
    clientId = os.environ.get("clientId")
    clientSecret = os.environ.get("clientSecret")
    return clientId, clientSecret

def getAPI(clientId, clientSecret):
    app_token = tk.request_client_token(clientId, clientSecret)
    spotifyAPI = tk.Spotify(app_token)
    return spotifyAPI

def getArtists(spotifyAPI):
    # get list of artists
    artistIds = []
    playlist = spotifyAPI.playlist_items("2V9ylS1wvL5xVwmmAMPKbM")
    for track in playlist.items:
        for artist in track.track.artists:
            artistIds.append(artist.id)
    return artistIds

def listGenres(spotifyAPI, artistIds):
    # get list of all genres
    genreList = []
    for artist_id in artistIds:
        currentArtist = spotifyAPI.artist(artist_id)
        for genre in currentArtist.genres:
            genreList.append(genre)
    genreList.sort()
    return genreList

def countGenres(genreList):
    # count occurences of each genre
    genreCounts = []
    for genre in genreList:
        count = genreList.count(genre)
        if [genre, count] not in genreCounts:
            genreCounts.append([genre, count])
    # sorts list by second item
    genreCounts.sort(key=lambda k: k[1], reverse=True)
    return genreCounts

def displayResult(genreCounts):
    print("placeholder")
    for genre in genreCounts:
        print(genre)
        print()

def main():
    clientId, clientSecret = loadEnvironment()
    spotifyAPI = getAPI(clientId, clientSecret)
    artistIds = getArtists(spotifyAPI)
    genreList = listGenres(spotifyAPI, artistIds)
    genreCounts = countGenres(genreList)
    displayResult(genreCounts)

if __name__ == '__main__':
    main()
