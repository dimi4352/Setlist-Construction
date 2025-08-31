import json
from pathlib import Path
import pandas as pd

df = pd.DataFrame(columns=["name", "path"])
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
            global df
            new_entry = {
                    folder.name : {"path":("{}".format(Folder_path.parent) + "\\" + "{}".format(Folder_path.name) + "\\" "{}".format(folder.name))
                }}
            df.loc[len(df)] = [folder.name, ("{}".format(Folder_path.parent) + "\\" + "{}".format(Folder_path.name) + "\\" "{}".format(folder.name))
                ]
            global inc
            inc += 1
            if inc >= 10000:
                print("{}".format(Folder_path))
                print(df)
                df.to_csv("JsonFiles&Paths_All.csv", mode='a', index=False, header=False)
                df = df[0:0]
                inc=0

        else: 
            print(folder.name)
            dummyFolder = "{}".format(Folder_path.parent) + "\\" + "{}".format(Folder_path.name) + "\\" + "{}".format(folder.name)
            searchStatsParent(dummyFolder)

searchStatsParent("\code\Masters\SetListThesis\Setlists\RecordingStats\High")

df.to_csv("JsonFiles&Paths_All.csv", mode='a', index=False, header=False)