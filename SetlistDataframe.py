#%%
import pandas as pd
import json
import numpy as np


 
with open("ArtistSetlistMBID.json", "r", encoding="utf-8") as f:
    mbidList = json.load(f)
#%%
df = pd.DataFrame(mbidList)
df.to_csv("ArtistSetlistMBID.csv")
#%%
with open("ArtistTourSet.json", "r", encoding="utf-8") as s:
    setlists = json.load(s)
#%%

#Finding the correct cell

def mbidFinder (artist,song,wanted):
    result = df.loc[(df['artist'] == artist) & (df['title'] == song), wanted].values
    if result.size > 0:
        value = result[0]
    else:
        value = None
    return value

#%%
#Creating the dataframe

rows = []
for artist, tours in setlists.items():
    for tour, concerts in tours.items():
        for concert in concerts:
            event_date = concert["eventDate"]
            venue = concert["venue"]
            city = concert["city"]
            country = concert["country"]
            ids=[]
            songs=[]
            hasEncore=0
            for set_data in concert["sets"]:
                if set_data["setName"] == "Encore":
                    hasEncore=1
                if len(set_data["songs"]) > 1:
                    for song in set_data["songs"]:
                        if song:  # ignore empty strings
                            mbid = mbidFinder(artist,song,"mbid")
                            song = mbidFinder(artist,song,"title")
                            songs.append(song)
                            ids.append(mbid)
            rows.append({
                "artist": artist,
                "tour": tour,
                "event_date": event_date,
                "venue": venue,
                "city": city,
                "country": country,
                "hasEncore": hasEncore,
                "setlist": ids,
                "songTitles": songs
                })
            
#%%
dfc = pd.DataFrame(rows)

#%%

#%%

#Checking for inconcistent length
for row in dfc.itertuples():
    if len(row.setlist) != len(row.songTitles):
        print("Inconsistency in row: ")
        print(row.Index)
        
print("All rows have same length between setlist and songTitles")
#%%
dfc.to_csv('ArtistSetlistMbidTitle.csv', index = False)

#%%

df_exploded = dfc.explode(['setlist', 'songTitles'])

#%%

df_ex = df_exploded.dropna()
originalLength = len(df_exploded)
newLength = len(df_ex)

print((originalLength-newLength))
print(len(df_exploded["setlist"].dropna()) == len(df_exploded["songTitles"].dropna()))

#%%
for row in df_exploded[["setlist","songTitles"]].itertuples():
    if row.setlist == row.songTitles and row.setlist == None and row.songTitles != None:
        print(row.songTitles)


#%%
dupe = df_ex.duplicated()

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("done")
print(counts)

#Artists sometimes play the same song again in the same setlist (check index 83 in dfc)
#%%
df_ex = df_ex.drop_duplicates()
df_ex.isnull().sum()

dupe = df_ex.duplicated()

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("done")
print(counts)

#%%

df_ex = df_ex.rename(columns={'setlist': 'mbid'})
#%%

df_ex.to_csv('ArtistSetlistMbidExpl.csv', index = False)