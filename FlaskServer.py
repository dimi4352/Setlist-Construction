from flask import Flask, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize the Flask app
app = Flask(__name__)


CLIENT_ID = '*************' # enter client Id
CLIENT_SECRET = '***************' # enter client secret id
REDIRECT_URI = 'http://localhost:8888/callback'

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-library-read playlist-read-private user-read-private user-read-email"
)

# Step 1: Redirect the user to Spotify for login
@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# Step 2: After user logs in, capture the authorization code from the redirect URL
@app.route('/callback')
def callback():
    token_info = sp_oauth.get_access_token(request.args['code'])
    access_token = token_info['access_token']
    refresh_token = token_info['refresh_token']
    
    print(f"Access Token: {access_token}")
    print(f"Refresh Token: {refresh_token}")
    
    # Use the token to make API requests
    sp = spotipy.Spotify(auth=access_token)
    user_info = sp.current_user()
    print(f"User Info: {user_info}")
    
    return 'Authorization successful! You can close this window.'

# Run the Flask server
if __name__ == '__main__':
    app.run(port=8888)
