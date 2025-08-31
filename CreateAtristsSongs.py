import json

# Load structured JSON data
with open("ArtistTourSet.json", "r", encoding="utf-8") as f:
    structuredData = json.load(f)

# Dictionary to store artist songs
artistSongs = {}

for artistName, tours in structuredData.items():
    songsSet = set()  # Using a set to avoid duplicates

    for tourName, concerts in tours.items():
        for concert in concerts:
            for setInfo in concert["sets"]:
                songsSet.update(setInfo["songs"])  # Add songs to the set
                if "" in songsSet:
                    songsSet.remove("")

    # Convert set to list and store in the dictionary
    artistSongs[artistName] = sorted(songsSet)  # Sorting for readability

# Save the final data to a new JSON file
with open("ArtistSongs.json", "w", encoding="utf-8") as f:
    json.dump(artistSongs, f, indent=4, ensure_ascii=False)


