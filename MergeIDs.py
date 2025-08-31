#%%
import pandas as pd
import json

#%%
fromAB = pd.read_csv("JsonFiles&Paths_All.csv")

#%%
with open('ArtistSetlistMBID.json', 'r', encoding='utf-8') as f:
    MBID = json.load(f)

data = []

for elem in MBID:
    data.append(elem["mbid"])
    
MBID = pd.DataFrame(data, columns=['mbid'])

# %%
fromAB.columns = ['mbid', 'path']

# %%

fromAB.loc[len(fromAB)] = ['000009a8-34f1-4c58-a8de-1d99809cd626-7.json', '\code\Masters\SetListThesis\Setlists\RecordingStats\High\highlevel1\00\0\000009a8-34f1-4c58-a8de-1d99809cd626-7.json'
]

#%%

fromAB['mbid36'] = fromAB['mbid'].str[:36]
#%%
fromAB.rename(columns={"mbid36":"mbid","mbid":"originMbid"},inplace=True)
# %%
fromAB.sort_values(by=["originMbid"],inplace=True,ignore_index=False)
fromAB_unique = fromAB.drop_duplicates(subset='mbid', keep='last')
# %%
InnerDf = pd.merge(fromAB_unique, MBID, on='mbid', how='inner')

# %%
MBID.to_csv("SetlistSongsIds.csv")
fromAB_unique.to_csv("UniqueABids.csv")
InnerDf.to_csv("MergedMBIDs.csv")
# %%
