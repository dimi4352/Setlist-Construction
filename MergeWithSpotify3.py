import pandas as pd
import json
import numpy as np


#%%
dfBig = pd.read_csv("MergeWithGetSong2.csv")


# Load JSON file
with open("TrackDataSpotify.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract rows into a list of dictionaries
rows = []
for artist, tracks in data.items():
    for track in tracks:
        details = track.get("track_details")
        if details.get("artist") is None:
            rows.append({
                "artist": artist,
                "song": track.get("song"),
                "popularity": None,
            })
        else:
            rows.append({
                 "artist": artist,
                 "song": track.get("song"),
                 "popularity": details.get("popularity"),
            })

dfSpot = pd.DataFrame(rows)
#%%
dfSpot = dfSpot.rename(columns={'song': 'songTitles'})

#%%

print(dfSpot.isnull().sum())

dfSpot = dfSpot.drop_duplicates(subset=['songTitles', 'artist'])

dupe = dfSpot.duplicated(subset=['songTitles', 'artist'])

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("duplicates: ")
print(counts)

dfSpot = dfSpot.drop_duplicates(subset=['songTitles', 'artist'])

#%%

merged_df = pd.merge(dfBig, dfSpot, on=['artist', 'songTitles'], how='left')


#%%
merged_df.to_csv("MergeWithSpotify3.csv",index=False)



