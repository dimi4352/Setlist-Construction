import json
import requests
import base64

CLIENT_ID = '*************' # enter client Id
CLIENT_SECRET = '***************' # enter client secret id

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

ACCESS_TOKEN = get_access_token()

def get_artist_id(artist_name):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    artists = response.get("artists", {}).get("items", [])
    if artists:
        return artists[0]["id"]  # First match
    return None

def get_artist_details(artist_name):
    artist_id = get_artist_id(artist_name)
    if not artist_id:
        return None
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    response = requests.get(url, headers=headers).json()
    return {
        "name": response.get("name"),
        "id": response.get("id"),
        "genres": response.get("genres"),
        "popularity": response.get("popularity"),
        "followers": response.get("followers", {}).get("total"),
    }

with open("ArtistNames.txt","r", encoding="utf-8") as names:
    artists = [line.strip() for line in names if line.strip()]

artist_details = {artist: get_artist_details(artist) for artist in artists}

# Save to JSON
with open("ArtistDetailsSpotify.json", "w") as f:
    json.dump(artist_details, f, indent=4)

print("Saved ArtistDetailsSpotify.json")
