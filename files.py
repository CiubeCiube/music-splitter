import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

inputFolder = "./data"
outputFolder = "./output"
tracklistFile = "./data/tracklist.json"

def checkSource():
  files = os.listdir(inputFolder)

  if len(files) > 2:
    print("Error: please insert only the source audio file and the tracklist file inside the data folder")
    return {"code": -1}

  audioFile = None
  tracklist = None

  for f in files:
    if f == "tracklist.json":
      tracklist = os.path.join(inputFolder, f)
    else:
      audioFile = os.path.join(inputFolder, f)

  if not tracklist:
    return {"code": 1}
  else:
    return {
      "code": 0,
      "data": {
        "source": audioFile,
        "config": tracklist
      }
    }

def downloadYTAudio(url):
  yt = YouTube(url, client='WEB_MUSIC', on_progress_callback=on_progress)

  userConfirm = input(f"Do you want to proceed to download the audio from the following video:\n{yt.title}\nNOTE: The following action will delete all the audio files in the folder {inputFolder}\n[Y/n]")

  if userConfirm == "" or userConfirm == "y" or userConfirm == "Y":
    files = os.listdir(inputFolder)
    for f in files:
      if f != "tracklist.json":
        filePath = os.path.join(inputFolder, f)
        os.remove(filePath)

    ys = yt.streams.get_audio_only()
    ys.download(output_path=inputFolder)
  else:
    print("Download aborted\n\n")