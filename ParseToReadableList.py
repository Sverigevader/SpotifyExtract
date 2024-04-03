import json

# This assumes you have a JSON file that directly contains an array of track items.
file_path = 'complete_spotify_playlist.json'
output_file_path = 'playlist_tracks.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    tracks_data = json.load(file)

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for item in tracks_data:
        # Directly access 'track' since the structure now is an array of items.
        track = item.get('track', {})
        if track:  # Checking if 'track' exists to avoid errors in case of empty or None
            track_name = track.get('name', 'Unknown Track')
            artist_names = [artist['name'] for artist in track.get('artists', [])]

            output_file.write(f"{', '.join(artist_names)} {track_name}\n")
        else:
            output_file.write("A track without details was encountered.\n")

print(f"Playlist tracks have been written to {output_file_path}")
