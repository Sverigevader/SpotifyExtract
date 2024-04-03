import json

import requests

# Your Spotify API credentials
client_id = '...'
client_secret = '...'
# The playlist you want to "backup"
playlist_id = '...'

# Function to get access token
def get_access_token(client_id, client_secret):
    auth_response = requests.post('https://accounts.spotify.com/api/token', {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

# Function to fetch all tracks from a playlist
def fetch_playlist_tracks(client_id, client_secret, playlist_id):
    access_token = get_access_token(client_id, client_secret)
    headers = {'Authorization': f'Bearer {access_token}'}
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    all_tracks = []

    while url:
        response = requests.get(url, headers=headers)
        data = response.json()
        all_tracks.extend(data['items'])
        url = data['next']  # URL for the next page, if any
    
    return all_tracks

# Fetch all tracks
all_tracks = fetch_playlist_tracks(client_id, client_secret, playlist_id)

# Save to file
with open('complete_spotify_playlist.json', 'w', encoding='utf-8') as file:
    json.dump(all_tracks, file)