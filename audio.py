from pydub import AudioSegment
import os
import json

from helpers import msTime
from files import outputFolder

def splitAudio(props):

  print("\n")

  source = props["source"]
  config = props["config"]

  input = AudioSegment.from_file(source)
  totalLen = len(input)

  ext = os.path.splitext(source)[1].lower()
  if ext in (".mp3"):
    exportFormat = "mp3"
    exportExt = "mp3"
    exportParams = []
  elif ext == ".m4a":
    exportFormat = "ipod"
    exportExt = "m4a"
    exportParams = []
  else:
    exportFormat = "flac"
    exportExt = "flac"
    exportParams = ["-compression_level", "5"]

  with open(config, "r") as configFile:
    data = json.load(configFile)

  tracklist = data["tracks"]
  artistName = data["artistName"]
  albumName = data["albumName"]
  albumDate = data["albumYear"]

  os.makedirs(outputFolder, exist_ok=True)

  for index, item in enumerate(tracklist):

    if index + 1 < len(tracklist):
      end = msTime(tracklist[index + 1]["start"])
    else:
      end = totalLen

    start = msTime(item["start"])

    segment = input[start:end]

    if exportFormat == "flac":
      segment = segment.set_frame_rate(44100).set_sample_width(2).set_channels(2)

    try:
      outPath = f"{outputFolder}/{str(index + 1).zfill(2)}. {item['name']}.{exportExt}"
      segment.export(
        outPath,
        format=exportFormat,
        parameters=exportParams,
        tags={
          "title": item["name"],
          "artist": artistName,
          "album": albumName,
          "tracknumber": str(index + 1),
          "date": albumDate,
          "genre": ""
        }
      )
      print(f"{outPath} done\n")
    except Exception as err:
      print(f"Error on track {index + 1}: {err}\n")