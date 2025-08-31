#%%
import json
import pandas as pd
import time
import requests

#%%
with open('ArtistSetlistMBID.json', 'r', encoding='utf-8') as f:
    MBID = json.load(f)

title = []
artist = []

for elem in MBID:
    title.append(elem["title"])
    artist.append(elem["artist"])
    
df = pd.DataFrame(title, columns=['title'])
df["artist"] = artist
#%%

df["title"] = df["title"].str.replace("%", "%25")
df["artist"] = df["artist"].str.replace("%", "%25")
df["title"] = df["title"].str.replace("&", "%26")
df["artist"] = df["artist"].str.replace("&", "%26")
df["title"] = df["title"].str.replace(" ", "%20")
df["artist"] = df["artist"].str.replace(" ", "%20")
df["title"] = df["title"].str.replace("#", "%23")
df["artist"] = df["artist"].str.replace("#", "%23")
df["title"] = df["title"].str.replace("’", "%27")
df["artist"] = df["artist"].str.replace("’", "%27")


API_KEY = "*********" # replace with api key
BASE_URL = "https://api.getsong.co"


def get_song_details(song,artist):
    url = f"{BASE_URL}/search/?api_key={API_KEY}&type=both&lookup=song%3A{song}%20artist%3A{artist}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

#%%
dice = {}
for index, row in df.iterrows():
        Ntitle = row['title']
        Nartist = row['artist']
        print(Ntitle, Nartist)
        data = get_song_details(Ntitle,Nartist).get('search', {})
        dice.update({index : {"getSong" : data}})
        time.sleep(2)
        print(index)
        with open("GetSongBPM.json", "w") as f:
            json.dump(dice, f, indent=4)
        


# %%
dfb = pd.DataFrame(dice)
dfb = pd.DataFrame.from_dict(dfb, orient='columns').T.reset_index(drop=True)


# %%
def normalize_single_song(row):
    song_data = row['getSong']
    if isinstance(song_data, list) and song_data:
        return pd.json_normalize(song_data[0])  # take first song only
    else:
        return pd.DataFrame([{}])  # or handle NaNs differently

# Process
expanded_df_list = []
for _, row in dfb.iterrows():
    normalized = normalize_single_song(row)
    expanded_df_list.append(normalized)

df_expanded = pd.concat(expanded_df_list, ignore_index=True)

df_expanded["Nartist"] = artist
df_expanded["Ntitle"] = title
# %%
print(df_expanded )
df_expanded = df_expanded.drop(columns=["Unnamed: 0"])
# %%
df_expanded.to_csv("GetSongBPM.csv")