import json
import requests
import base64

CLIENT_ID = "a4d01f7a367f49da89eac2fdfb22b738"
CLIENT_SECRET = "b472bb81d5f54b139b34f813ba50dba0"

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

ACCESS_TOKEN = "**********" #input access token manualy
#get_access_token()

def get_track_id_by_song(song):
    url = f"https://api.spotify.com/v1/search?q=track:{song}&type=track"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    tracks = response.get("tracks", {}).get("items", [])
    
    if tracks:
        return tracks[0]["id"]  # First result's ID
    return None

def get_track_id(artist, song):
    url = f"https://api.spotify.com/v1/search?q=track:{song}%20artist:{artist}&type=track"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    tracks = response.get("tracks", {}).get("items", [])
    if tracks:
        result = tracks[0]["id"]
    else:
        result = "cover"
    return result


def get_track_details(track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    return {
        "name": response.get("name"),
        "popularity": response.get("popularity"),
        "album": response.get("album", {}).get("name"),
        "release_date": response.get("album", {}).get("release_date"),
        "artist": response.get("artists", [{}])[0].get("name")
    }



with open("ArtistSongs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)


track_data = {}

for artist, song_list in songs.items():
    track_data[artist] = []
    for song in song_list:
        cover = False
        track_id = get_track_id(artist, song)
        print(f"🔍 Found Track ID for {artist} - {song}: {track_id}")
        if track_id:
            track_details = get_track_details(track_id)
            track_data[artist].append({"song": song, "track_details": track_details, "cover": cover})
        else :
            cover = True
            track_id = get_track_id_by_song(song)
            if track_id:
                track_details = get_track_details(track_id)
                track_data[artist].append({"song": song, "track_details": track_details, "cover": cover})
            else:
                print(f"❌ Track not found: {artist} - {song}")

# Save to JSON
with open("TrackDataSpotify.json", "w") as f:
    json.dump(track_data, f, indent=4)

print("Saved TrackDataSpotify.json ✅")


