import json
import pandas as pd
import time

start_time = time.time()


IdsCsv = pd.read_csv("MergedMBIDs.csv")

df = pd.DataFrame(columns=["id", "title", "atrist", "year", "bpm",
        "danceability","danceabilityP", "genre_dortmund", "genre_dortmundP",
        "genre_rosamerica", "genre_rosamericaP","genre_tzanetakis",
        "genre_tzanetakisP", "ismir04_rhythm", "ismir04_rhythmP",
        "mood_acoustic", "mood_acousticP", "mood_aggressive", "mood_aggressiveP",
        "mood_electronic", "mood_electronicP", "mood_happy", "mood_happyP",
        "mood_party", "mood_partyP", "mood_relaxed", "mood_relaxedP", 
        "mood_sad", "mood_sadP", "mood_electronic", "mood_electronicP",
        "moods_mirex", "moods_mirexP", "timbre", "timbreP", 
        "tonal_atonal", "tonal_atonalP", "voice_instrumental",
        "voice_instrumentalP", "gender", "genderP" , "path"])
inc = 0
    

for _,row in IdsCsv.iterrows():
    ids = row["mbid"] 
    pathing = row["path"] 
    inc = inc + 1
    print(inc)

    with open(pathing, 'r', encoding='utf-8') as f:  #, errors='replace'
        artist_data = f.read()#.replace('\x00', '')

    data = json.loads(artist_data)

    if (data["metadata"] != None) and (data["metadata"]["tags"] != None) and (data["highlevel"] != None):
        if ("title" in data.get("metadata", {}).get("tags", {})) :
            title=data["metadata"]["tags"]["title"][0]
        else:
            title=None
        if ("artist" in data.get("metadata", {}).get("tags", {})):
            artist=data["metadata"]["tags"]["artist"][0]
        else:
            artist=None
        if ("originalyear" in data.get("metadata", {}).get("tags", {})) :
            originalyear=data["metadata"]["tags"]["originalyear"][0]
        else:
            originalyear=None
        if ("bpm" in data.get("metadata", {}).get("tags", {})) :
            BPM=data["metadata"]["tags"]["bpm"][0]
        else:
            BPM=None
        if ("initialkey" in data.get("metadata", {}).get("tags", {})) :
            initialkey=data["metadata"]["tags"]["initialkey"][0]
        else:
            initialkey=None

        if ("danceability" in data.get("highlevel", {})) :
            danceability=data["highlevel"]["danceability"]["value"]
            danceabilityP=data["highlevel"]["danceability"]["probability"]
        else:
            danceability=None
            danceabilityP=None
        if ("genre_dortmund" in data.get("highlevel", {})) :
            genre_dortmund=data["highlevel"]["genre_dortmund"]["value"]
            genre_dortmundP=data["highlevel"]["genre_dortmund"]["probability"]
        else:
            genre_dortmund=None
            genre_dortmundP=None
        if ("genre_rosamerica" in data.get("highlevel", {})) :
            genre_rosamerica=data["highlevel"]["genre_rosamerica"]["value"]
            genre_rosamericaP=data["highlevel"]["genre_rosamerica"]["probability"]
        else:
            genre_rosamerica=None
            genre_rosamericaP=None
        if ("genre_tzanetakis" in data.get("highlevel", {})) :
            genre_tzanetakis=data["highlevel"]["genre_tzanetakis"]["value"]
            genre_tzanetakisP=data["highlevel"]["genre_tzanetakis"]["probability"]
        else:
            genre_tzanetakis=None
            genre_tzanetakisP=None
        if ("ismir04_rhythm" in data.get("highlevel", {})) :
            ismir04_rhythm=data["highlevel"]["ismir04_rhythm"]["value"]
            ismir04_rhythmP=data["highlevel"]["ismir04_rhythm"]["probability"]
        else:
            ismir04_rhythm=None
            ismir04_rhythmP=None
        if ("mood_acoustic" in data.get("highlevel", {})) :
            mood_acoustic=data["highlevel"]["mood_acoustic"]["value"]
            mood_acousticP=data["highlevel"]["mood_acoustic"]["probability"]
        else:
            mood_acoustic=None
            mood_acousticP=None
        if ("mood_aggressive" in data.get("highlevel", {})) :
            mood_aggressive=data["highlevel"]["mood_aggressive"]["value"]
            mood_aggressiveP=data["highlevel"]["mood_aggressive"]["probability"]
        else:
            mood_aggressive=None
            mood_aggressiveP=None
        if ("mood_electronic" in data.get("highlevel", {})) :
            mood_electronic=data["highlevel"]["mood_electronic"]["value"]
            mood_electronicP=data["highlevel"]["mood_electronic"]["probability"]
        else:
            mood_electronic=None
            mood_electronicP=None
        if ("mood_happy" in data.get("highlevel", {})) :
            mood_happy=data["highlevel"]["mood_happy"]["value"]
            mood_happyP=data["highlevel"]["mood_happy"]["probability"]
        else:
            mood_happy=None
            mood_happyP=None
        if ("mood_party" in data.get("highlevel", {})) :
            mood_party=data["highlevel"]["mood_party"]["value"]
            mood_partyP=data["highlevel"]["mood_party"]["probability"]
        else:
            mood_party=None
            mood_partyP=None
        if ("mood_party" in data.get("highlevel", {})) :
            mood_relaxed=data["highlevel"]["mood_relaxed"]["value"]
            mood_relaxedP=data["highlevel"]["mood_relaxed"]["probability"]
        else:
            mood_relaxed=None
            mood_relaxedP=None
        if ("mood_sad" in data.get("highlevel", {})) :
            mood_sadP=data["highlevel"]["mood_sad"]["probability"]
            mood_sad=data["highlevel"]["mood_sad"]["value"]
        else:
            mood_sad=None
            mood_sadP=None
        if ("mood_sad" in data.get("highlevel", {})) :
            mood_electronic=data["highlevel"]["mood_electronic"]["value"]
            mood_electronicP=data["highlevel"]["mood_electronic"]["probability"]
        else:
            mood_electronic=None
            mood_electronicP=None
        if ("moods_mirex" in data.get("highlevel", {})) :
            moods_mirex=data["highlevel"]["moods_mirex"]["value"]
            moods_mirexP=data["highlevel"]["moods_mirex"]["probability"]
        else:
            moods_mirex=None
            moods_mirexP=None
        if ("timbre" in data.get("highlevel", {})) :
            timbre=data["highlevel"]["timbre"]["value"]
            timbreP=data["highlevel"]["timbre"]["probability"]
        else:
            timbre=None
            timbreP=None
        if ("tonal_atonal" in data.get("highlevel", {})) :
            tonal_atonal=data["highlevel"]["tonal_atonal"]["value"]
            tonal_atonalP=data["highlevel"]["tonal_atonal"]["probability"]
        else:
            tonal_atonal=None
            tonal_atonalP=None
        if ("voice_instrumental" in data.get("metadata", {}).get("tags", {})) :
            voice_instrumental=data["highlevel"]["voice_instrumental"]["value"]
            voice_instrumentalP=data["highlevel"]["voice_instrumental"]["probability"]
        else:
            voice_instrumental=None
            voice_instrumentalP=None
        if ("gender" in data.get("highlevel", {})) :
            gender=data["highlevel"]["gender"]["value"]
            genderP=data["highlevel"]["gender"]["probability"]
        else:
            gender=None
            genderP=None

        


        putIn = {"id": ids, "title": title, "atrist": artist, "year": originalyear, "bpm": BPM,
        "danceability": danceability,"danceabilityP": danceabilityP, "genre_dortmund": genre_dortmund, "genre_dortmundP": genre_dortmundP,
        "genre_rosamerica": genre_rosamerica, "genre_rosamericaP": genre_rosamericaP,"genre_tzanetakis": genre_tzanetakis,
        "genre_tzanetakisP": genre_tzanetakisP, "ismir04_rhythm": ismir04_rhythm, "ismir04_rhythmP": ismir04_rhythmP,
        "mood_acoustic": mood_acoustic, "mood_acousticP": mood_acousticP, "mood_aggressive": mood_aggressive, "mood_aggressiveP": mood_aggressiveP,
        "mood_electronic": mood_electronic, "mood_electronicP": mood_electronicP, "mood_happy": mood_happy, "mood_happyP": mood_happyP,
        "mood_party": mood_party, "mood_partyP": mood_partyP, "mood_relaxed": mood_relaxed, "mood_relaxedP": mood_relaxedP, 
        "mood_sad": mood_sad, "mood_sadP": mood_sadP, "mood_electronic": mood_electronic, "mood_electronicP": mood_electronicP,
        "moods_mirex": moods_mirex, "moods_mirexP": moods_mirexP, "timbre": timbre, "timbreP": timbreP, 
        "tonal_atonal": tonal_atonal, "tonal_atonalP": tonal_atonalP, "voice_instrumental": voice_instrumental,
        "voice_instrumentalP": voice_instrumentalP, "gender": gender, "genderP": genderP, "path": pathing}

    else :
        putIn = {}
    df.loc[len(df)] = putIn

df = df.drop(columns=["Unnamed: 0"])
df.to_csv("UniqueSongData.csv")



end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time) 