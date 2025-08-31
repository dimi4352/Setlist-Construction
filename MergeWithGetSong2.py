import pandas as pd
import numpy as np

#%%
dfBig = pd.read_csv("MergeWithAB1.csv")

dfGet = pd.read_csv("GetSongBPM.csv")


#%%
dfGet = dfGet.rename(columns={'Ntitle': 'songTitles', 'Nartist': 'artist'})

#%%

print(dfGet.isnull().sum())

dfGet = dfGet.drop_duplicates(subset=['songTitles', 'artist'])

dupe = dfGet.duplicated(subset=['songTitles', 'artist'])

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("duplicates: ")
print(counts)

dfGet = dfGet.drop_duplicates(subset=['songTitles', 'artist'])

#%%

merged_df = pd.merge(dfBig, dfGet, on=['artist', 'songTitles'], how='left')

#%%

merged_df['bpm'] = merged_df['bpm'].replace(0, None)
#%%
merged_df= merged_df.rename(columns={'danceability_x': 'danceabilityAB',
                              'danceability_y': 'danceabilityG',
                              'artist.genres': 'artistGenres'})

cleanDf = merged_df.drop(columns=[
       'Unnamed: 0', 'id', 'title', 'uri',
       'open_key', 'artist.id',
       'artist.name', 'artist.uri', 'artist.from',
       'artist.mbid', 'album.title', 'album.uri', 'album.year'])

#%%
cleanDf.to_csv("MergeWithGetSong2.csv",index=False)
