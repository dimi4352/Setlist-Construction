import requests
import json
import requests
import base64
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "*************" #e nter client id
CLIENT_SECRET = "************" #enter client secrete id

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

#ACCESS_TOKEN = get_access_token()
ACCESS_TOKEN = "BQAN0YCSA1iQu7QuyI1AcESmjx0OME3b4-RNQu2vJXOIMXXojVBWApfifVF1zjkkRXXs76ivdgcmrJPyVkP20UCQmI4Bs8jiRSKHBgwe29VjQMe3useWTYyFXZQRQLGCmvkkCUuuHNnz2DluchiJevDBz-HugDJkT3n_UdnPPzIB8VCoo9md-chpiLGKaRPWsLqlUCekRF21QoXkDuhri1nREyqcrZ_h6AlESQVElS6n2KRCTjVp18OGY_Ki79Rg_BVljOfeBHzqzlwCdlnD_4_7R7LZkqknoTE59-UX3cMRKhMA"

def check_access_token(access_token):
    url = "https://api.spotify.com/v1/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("✅ Token is valid!")
        return True
    elif response.status_code == 401:  # Unauthorized (expired token)
        print("❌ Token is invalid or expired. Please refresh it.")
        return False
    else:
        print(f"⚠️ Unexpected error: {response.json()}")
        return False

# Test your token
check_access_token(ACCESS_TOKEN)

token_info = sp_oauth.get_access_token(request.args['code'])
access_token = token_info['access_token']

# Verify the granted scopes
print(f"Granted Scopes: {token_info['scope']}")
