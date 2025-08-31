import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = '*************' # enter client Id
CLIENT_SECRET = '***************' # enter client secret id
REDIRECT_URI = 'http://localhost:8888/callback'

# Set up SpotifyOAuth object
sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-read-private user-read-private user-read-email"
)

# Step 1: Get the authorization URL
auth_url = sp_oauth.get_authorize_url()
print(f"Please go to this URL and authorize the app: {auth_url}")

# Step 2: User enters the authorization code after login
code = input("Enter the authorization code: ")

# Step 3: Get access and refresh tokens
token_info = sp_oauth.get_access_token(code)
access_token = token_info['access_token']
refresh_token = token_info['refresh_token']
print(f"Access Token: {access_token}")
print(f"Refresh Token: {refresh_token}")

# Step 4: Make an API call using the access token
sp = spotipy.Spotify(auth=access_token)
user_info = sp.current_user()
print(f"User Info: {user_info}")

# Step 5: Refresh the access token if needed
new_token_info = sp_oauth.refresh_access_token(refresh_token)
new_access_token = new_token_info['access_token']
print(f"New Access Token: {new_access_token}")

token_info = sp_oauth.get_access_token(request.args['code'])
access_token = token_info['access_token']

# Verify the granted scopes
print(f"Granted Scopes: {token_info['scope']}")
