import musicbrainzngs
import json
import time

musicbrainzngs.set_useragent("MusicBrainz", "1.0", "email") # replace email

def search_artist(name):
    try:
        result = musicbrainzngs.search_artists(artist=name, limit=1)
        if result["artist-list"]:
            artist = result["artist-list"][0]
            ArtistsMBdata [artist['name']] = artist
            ArtistsMBID [artist['name']] = artist['id']
        else:
            print("Artist not found.")
    except musicbrainzngs.WebServiceError as e:
        print(f"Error: {e}")

ArtistsMBID = {}
ArtistsMBdata ={}

with open("ArtistNames.txt", "r", encoding="utf-8") as file:
    for artist in file:
        print(artist)
        search_artist(artist.strip())
        time.sleep(2)


with open("ArtistsMBID.json", "w") as file:
    json.dump(ArtistsMBID, file, indent=4)

with open("ArtistsMBdata.json", "w") as file:
    json.dump(ArtistsMBdata, file, indent=4)
