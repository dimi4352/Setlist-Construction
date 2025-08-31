import json
import requests


with open("ArtistsMBID.json", "r") as file:
    ArtistsMBID = json.load(file)

failedToRetrieve = 0


API_KEY = "**************" # personal setlist.fm API-key  
HEADERS = {
    "x-api-key": API_KEY,
    "Accept": "application/json"
}

# Dictionary to store raw responses
rawData = {}

for artistName, mbid in ArtistsMBID.items():
    print(f"Fetching data for {artistName}...")
    url = f"https://api.setlist.fm/rest/1.0/artist/{mbid}/setlists"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Failed to get data for {artistName}. Status Code: {response.status_code}")
        failedToRetrieve += 1
        continue

    # Store raw API response
    rawData[artistName] = response.json()

if failedToRetrieve != 0:
    print("Failed to retrieve " + failedToRetrieve + " artists.")
else:
    print("Operation successful")

with open("rawSetlists.json", "w", encoding="utf-8") as f:
    json.dump(rawData, f, indent=4, ensure_ascii=False)
