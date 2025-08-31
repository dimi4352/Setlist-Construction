import json

# Load both JSON files
with open('ArtistSongs.json', 'r', encoding='utf-8') as f1:
    artist_songs = json.load(f1)

with open('AllArtistsRecordings.json', 'r',encoding='utf-8') as f2:
    artist_data = json.load(f2)

# Result container
combined_data = []

# Loop through artists and their songs
for artist, songs in artist_songs.items():
    if artist not in artist_data:
        continue

    recordings = artist_data[artist]
    for song_title in songs:
        # Try to find a matching title in the second file's data
        for recording in recordings:
            if recording['title'].strip().lower() == song_title.strip().lower():
                combined_data.append({
                    "artist": artist,
                    "title": song_title,
                    "mbid": recording.get("mbid")
                })
                break


with open('ArtistSetlistMBID.json', 'w') as out_file:
    json.dump(combined_data, out_file, indent=2)
