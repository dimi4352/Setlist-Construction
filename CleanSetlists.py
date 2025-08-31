import json

# Load raw JSON data
with open("rawSetlists.json", "r", encoding="utf-8") as f:
    rawData = json.load(f)

# Dictionary to store structured data
structuredData = {}

for artistName, artistSetlists in rawData.items():
    structuredData[artistName] = {}

    for setlist in artistSetlists.get("setlist", []):
        tourName = setlist.get("tour", {}).get("name", "Unknown Tour")
        eventDate = setlist["eventDate"]
        venueName = setlist["venue"]["name"]
        city = setlist["venue"]["city"]["name"]
        country = setlist["venue"]["city"]["country"]["code"]

        # Initialize tour if not present
        if tourName not in structuredData[artistName]:
            structuredData[artistName][tourName] = []

        # Extract sets and songs
        setsData = []
        for setInfo in setlist.get("sets", {}).get("set", []):
            setName = setInfo.get("name", "").strip() or "Encore"
            songs = [song["name"] for song in setInfo.get("song", [])]
            if setName == "Encore" and len(songs) > 3:
                setName = "Main Set"

            setsData.append({
                "setName": setName,
                "songs": songs
            })

        # Add concert details
        structuredData[artistName][tourName].append({
            "eventDate": eventDate,
            "venue": venueName,
            "city": city,
            "country": country,
            "sets": setsData
        })

# Save structured data to a new JSON file
with open("ArtistTourSet.json", "w", encoding="utf-8") as f:
    json.dump(structuredData, f, indent=4, ensure_ascii=False)




