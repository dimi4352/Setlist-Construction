import requests
import base64

# Spotify API credentials
CLIENT_ID = '*************' # enter client Id
CLIENT_SECRET = '***************' # enter client secret id
REFRESH_TOKEN = "AQAzJPp_IcD72e9bxbRvezjxFqEjZ0nz2wYjgSL-zTF-M5fndKcd-TKo835ZM-Gx10kILhWT45_70vgXUZZGgPcpwmGH9K8Fn3RPuyQFuQANuv9rYsVgYj4boirmGZijbPw"

# Spotify token endpoint
TOKEN_URL = "https://accounts.spotify.com/api/token"

def refresh_access_token():
    # Encode client ID and secret
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    b64_client_creds = base64.b64encode(client_creds.encode()).decode()
    headers = {
        "Authorization": f"Basic {b64_client_creds}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    }

    response = requests.post(TOKEN_URL, headers=headers, data=data)
    response_data = response.json()

    if "access_token" in response_data:
        new_access_token = response_data["access_token"]
        print("New Access Token:", new_access_token)
        return new_access_token
    else:
        print("Error refreshing token:", response_data)
        return None

access_token = refresh_access_token()
