import pandas as pd
import json
import numpy as np
import ast



#%%
dfBig = pd.read_csv("MergeWithSpotify3.csv")


def changeProbability (binaryCol,probCol,determinator):  
    inc = 0
    for elem in dfBig[binaryCol]:
        if elem != None and elem == determinator:
            dfBig.loc[inc, probCol] = round(1.00 - dfBig.loc[inc, probCol],6)
        elif elem != None:
            dfBig.loc[inc, probCol] = dfBig.loc[inc, probCol]
        inc = inc + 1
        
            
#%%
changeProbability('danceabilityAB','danceabilityP','not_danceable')
changeProbability('mood_acoustic','mood_acousticP','not_acoustic')
changeProbability('mood_aggressive','mood_aggressiveP','not_aggressive')
changeProbability('mood_electronic','mood_electronicP','not_electronic')
changeProbability('mood_happy','mood_happyP','not_happy')
changeProbability('mood_party','mood_partyP','not_party')
changeProbability('mood_relaxed','mood_relaxedP','not_relaxed')
changeProbability('mood_sad','mood_sadP','not_sad')
changeProbability('timbre','timbreP','dark')
#%%
dfb = dfBig.copy()

dfb['danceabilityP'] = dfb['danceabilityP'] * 100
dfb['mood_acousticP'] = dfb['mood_acousticP'] * 100
#%%

dfb['bpm'] = dfb[['tempo', 'bpm']].mean(axis=1)
dfb['danceability'] = dfb[['danceabilityP', 'danceabilityG']].mean(axis=1)
dfb['acousticness'] = dfb[['acousticness','mood_acousticP']].mean(axis=1)

#%%

dfb = dfb.drop(columns=['danceabilityAB', 'danceabilityP',
        'mood_acoustic', 'mood_acousticP', 'mood_aggressive',
        'mood_electronic',  'mood_happy',
        'mood_party',  'mood_relaxed',
        'mood_sad',  'timbre',  'tempo',
        'danceabilityG'])
#%%
dfb = dfb.rename(columns={'mood_aggressiveP': 'mood_aggressive',
                        'mood_electronicP': 'mood_electronic',
                        'mood_happyP': 'mood_happy',
                        'mood_partyÆ': 'mood_party', 
                        'mood_relaxedP': 'mood_relaxed',
                        'mood_sadP': 'mood_sad','timbreP': 'timbre'})

#%%

print(dfb.isnull().sum())


dupe = dfb.duplicated()

counts = 0
for row in dupe:
 if row == True:
    counts = counts +1
    
print("duplicates: ")
print(counts)



#%%
dfb.to_csv("MergeCleaningFinal4.csv",index=False)

