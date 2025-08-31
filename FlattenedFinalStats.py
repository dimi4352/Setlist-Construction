import pandas as pd
import json
import numpy as np
import ast



#%%
dfBig = pd.read_csv("MergeCleaningFinal4.csv")

dfSet = pd.read_csv("ArtistSetlistMbidTitle.csv")
        
            
#%%
group_cols = ['artist', 'tour', 'event_date', 'venue', 'city', 'country', 'hasEncore']

#Columns to be aggregated into lists
agg_cols = [
    'mbid', 'songTitles', 'bpm', 'ismir04_rhythm', 'mood_aggressive',
    'mood_electronic', 'mood_happy', 'mood_partyP', 'mood_relaxed',
    'mood_sad', 'timbre', 'time_sig', 'key_of', 'acousticness',
    'popularity', 'danceability'
]

#Dictionary for the aggregation
agg_dict = {col: lambda x: list(x) for col in agg_cols}

# Groupby
df_grouped = dfBig.groupby(group_cols).agg(agg_dict).reset_index()


#%%
df=dfSet.copy()

print((df['setlist'] == '[]').sum())
print((df['songTitles'] == '[]').sum())

print((len(dfSet)-len(df_grouped)))

print((len(dfSet)-len(df_grouped) == ((df['setlist'] == '[]').sum().astype(int))))
#%%

df=df[df.setlist != '[]']


#%%
'''
count = 0
for cell in df['setlist']:
    if len(ast.literal_eval(cell)) == 1:
        count = count+1
print(count)


#%%

one = sorted(df["event_date"].tolist())
two = sorted(df_grouped["event_date"].tolist())

for x in range(2241):
    if one[x] != two[x]:
        print(x)
        print(one[x])
        print(two[x])
        print(one[x-1])
        print(two[x-1])
        break
'''


#%%
df = df.drop_duplicates(subset=["venue","artist","event_date","tour"])

#%%




#%%
df_grouped.to_csv("FlattenedFinalStats.csv",index=False)



