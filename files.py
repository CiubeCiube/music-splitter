import os

outputFolder = "./output"
tracklistFile = "./data/tracklist.json"

def checkSource():
  folder = "./data"
  files = os.listdir(folder)

  if len(files) > 2:
    print("Error: please insert only the source audio file and the tracklist file inside the data folder")
    return {"code": -1}

  audioFile = None
  tracklist = None

  for f in files:
    if f == "tracklist.json":
      tracklist = os.path.join(folder, f)
    else:
      audioFile = os.path.join(folder, f)

  if not audioFile or not tracklist:
    return {"code": 1}
  else:
    return {
      "code": 0,
      "data": {
        "source": audioFile,
        "config": tracklist
      }
    }