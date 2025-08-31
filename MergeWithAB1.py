import pandas as pd
import numpy as np

#%%
dfAB = pd.read_csv("UniqueSongData.csv")

dfSet = pd.read_csv("ArtistSetlistMbidExpl.csv")

#%%

AB = len(dfAB)

Set = len(dfSet)

#%%
dfAB = dfAB.rename(columns={'title': 'songTitles', 'id':'mbid', 'atrist': 'artist'})

#%%

dfAB.isnull().sum()

dfAB = dfAB.drop_duplicates(subset=['songTitles', 'mbid', 'artist'])

dupe = dfAB.duplicated(subset=['songTitles', 'mbid', 'artist'])

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("duplicates: ")
print(counts)



#%%

merged_df = pd.merge(dfSet, dfAB, on=['artist', 'songTitles', 'mbid'], how='left')

#%%

merged_df['bpm'] = merged_df['bpm'].replace(0, None)

cleanDf = merged_df.drop(columns=['Unnamed: 0', 'year',  'genre_dortmund', 'genre_dortmundP',
       'genre_rosamerica', 'genre_rosamericaP', 'genre_tzanetakis',
       'genre_tzanetakisP', 'ismir04_rhythmP','mood_electronic.1',
       'mood_electronicP.1', 'moods_mirex', 'moods_mirexP',
       'tonal_atonal', 'tonal_atonalP', 'voice_instrumental',
       'voice_instrumentalP', 'gender', 'genderP', 'path'])

#%%
cleanDf.to_csv("MergeWithAB1.csv",index=False)
