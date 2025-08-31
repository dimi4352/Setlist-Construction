import musicbrainzngs
import json
import time

# Initialize MusicBrainz API
musicbrainzngs.set_useragent("MusicBrainz", "1.0", "email") # replace email


# Load artist MBIDs from your JSON file
with open("ArtistsMBID.json", "r", encoding="utf-8") as f:
    artist_mbid_dict = json.load(f)

# Fetch all recordings by artist MBID
def fetch_all_recordings(artist_mbid):
    recordings = []
    limit = 100
    offset = 0

    while True:
        result = musicbrainzngs.browse_recordings(artist=artist_mbid, limit=limit, offset=offset)
        recordings.extend(result['recording-list'])
        if len(result['recording-list']) < limit:
            break
        offset += limit
    return recordings

# Filter for unique titles
def filter_unique_titles(recordings):
    seen = set()
    unique = []
    for rec in recordings:
        title = rec['title'].lower()
        if title not in seen:
            seen.add(title)
            unique.append({
                "title": rec['title'],
                "mbid": rec['id'],
                "length": int(rec.get('length', 0)) / 1000 if 'length' in rec else None,
                "artist": ", ".join([a['artist']['name'] for a in rec.get('artist-credit', [])]) if 'artist-credit' in rec else "Unknown"

            })
    return unique

# Detect if recording is a cover or original
def detect_possible_cover(recording_mbid):
    try:
        result = musicbrainzngs.get_recording_by_id(recording_mbid, includes=["work-rels", "artist-credits"])
        recording = result['recording']
        artist_name = recording['artist-credit'][0]['artist']['name']

        if 'work-relation-list' in recording:
            for work_rel in recording['work-relation-list']:
                work = work_rel['work']
                if 'artist-relation-list' in work:
                    composers = [rel['artist']['name'] for rel in work['artist-relation-list']]
                    if artist_name.lower() not in [c.lower() for c in composers]:
                        return f"Yes: {', '.join(composers)}"
            return "No"
        else:
            return "Undefinable"
    except musicbrainzngs.WebServiceError as e:
        return f"Error: {e}"

# Main processing
all_artists_recordings = {}

for artist_name, mbid in artist_mbid_dict.items():

    try:
        all_recordings = fetch_all_recordings(mbid)
        

        unique_recordings = filter_unique_titles(all_recordings)

        for rec in unique_recordings:
            rec["cover"] = detect_possible_cover(rec["mbid"])
            

        all_artists_recordings[artist_name] = unique_recordings

        time.sleep(2)

    except Exception as e:
        print(f"⚠️ Error processing {artist_name}: {e}")
        all_artists_recordings[artist_name] = f"Error: {str(e)}"

# Save everything into one JSON file
with open("AllArtistsRecordings.json", "w", encoding="utf-8") as f:
    json.dump(all_artists_recordings, f, indent=4)


