import os
import subprocess

# Path to your list of songs
song_list_path = 'playlist_tracks.txt'

# Directory where you want to save the downloaded songs
download_directory = 'downloaded_songs'
os.makedirs(download_directory, exist_ok=True)

with open(song_list_path, 'r', encoding='utf-8') as file:
    for line in file:
        # Constructing the search query from each line
        search_query = line.strip().replace("|", "-")  # Basic cleanup
        
        # Download command using yt-dlp
        command = [
            'yt-dlp',
            '-x',  # Extract audio only
            '--audio-format', 'mp3',  # Convert to mp3
            '--audio-quality', '0',  # Best quality
            '--output', os.path.join(download_directory, '%(title)s.%(ext)s'),  # Output path
            f"ytsearch1:{search_query}"  # Search query, "ytsearch1:" searches for the first result
        ]
        
        # Execute the download command
        subprocess.run(command)

print("Download process complete.")
