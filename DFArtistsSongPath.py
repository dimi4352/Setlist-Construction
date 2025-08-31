import json
from pathlib import Path
#nonfunctioningS

data = {}
inc = 0


def searchStatsParent(Pathing):
    Folder_path = Path(Pathing)
    highlevelFolders = list(Folder_path.glob("*")) 
    for folder in highlevelFolders:
        if (folder.name.startswith(("acoust", "high",))):
            print(folder.name)
            dummyFolder = "{}".format(Folder_path.parent) + "\\" + "{}".format(Folder_path.name) + "\\" "{}".format(folder.name)
            searchStatsParent(dummyFolder)
        elif ((folder.name.startswith("COPY"))):
            continue
        elif folder.name.endswith(".json") :
            with open(folder, 'r',encoding='utf-8') as f2:
                artist_data = json.load(f2)
            if (artist_data["metadata"] != None) and (artist_data["metadata"]["tags"] != None):
                recording_id = artist_data["metadata"]["tags"]["musicbrainz_recordingid"][0]
                path_name = "{}".format(Folder_path) + "\\" + "{}".format(folder.name)
                if ("artist" in artist_data.get("metadata", {}).get("tags", {})):
                    artist_name = artist_data["metadata"]["tags"]["artist"][0] 
                else: 
                    artist_name = "unknown"
                new_entry = {
                    recording_id: {
                        "artist": artist_name,
                        "path": path_name
                    }
                }
                data.update(new_entry)
                global inc
                inc += 1
                if inc >= 5000:
                    print("{}".format(Folder_path))
                    with open('ABIDS.json', 'w') as out_file:
                        json.dump(data, out_file, indent=2)
                    out_file.close()
                    inc=0
            f2.close()
        else: 
            print(folder.name)
            dummyFolder = "{}".format(Folder_path.parent) + "\\" + "{}".format(Folder_path.name) + "\\" + "{}".format(folder.name)
            searchStatsParent(dummyFolder)

searchStatsParent("\code\Masters\SetListThesis\Setlists\RecordingStats\High")

