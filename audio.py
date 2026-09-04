from pydub import AudioSegment
import os
import json

from helpers import msTime
from files import outputFolder

def splitAudio(props):
  source = props["source"]
  config = props["config"]

  input = AudioSegment.from_file(source)
  totalLen = len(input)

  with open(config, "r") as configFile:
    data = json.load(configFile)

  tracklist = data["tracks"]
  artistName = data["artistName"]
  albumName = data["albumName"]
  albumDate = data["albumYear"]

  os.makedirs(outputFolder, exist_ok = True)

  for index, item in enumerate(tracklist):

    if index + 1 < len(tracklist):
      end = msTime(tracklist[index + 1]["start"])
    else:
      end = totalLen

    start = msTime(item["start"])

    segment = input[start:end]
    segment = segment.set_frame_rate(44100).set_sample_width(2).set_channels(2)

    try:
      segment.export(
        f"{outputFolder}/{str(index + 1)}. {item["name"]}.flac",
        format="flac",
        parameters=["-compression_level", "5"],
        tags={
          "title": item["name"],
          "artist": artistName,
          "album": albumName,
          "tracknumber": str(index + 1),
          "date": albumDate,
          "genre": ""
        }
      )
      message = f"\n{outputFolder}/{str(index + 1)}. {item["name"]}.flac done\n"
    except Exception as err:
      message = err

    print(message)