import json
import re

from files import tracklistFile

def msTime(time_str):
  parts = str(time_str).split(":")
  if len(parts) == 3:
    hours, minutes, seconds = int(parts[0]), int(parts[1]), int(parts[2])
  elif len(parts) == 2:
    hours, minutes, seconds = 0, int(parts[0]), int(parts[1])
  else:
    raise ValueError(f"Invalid time format: {time_str}")
  return (hours * 3600 + minutes * 60 + seconds) * 1000

def populateConfig():
  artistName = input("Artist Name: ")
  albumName = input("Album Name: ")
  albumYear = input("Album Year: ")

  print("Tracks (press Enter twice when done): ")
  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)

  tracks = []
  for line in lines:
    match = re.match(r"^\[(\d+(?::\d+)+)\]\s+(.+)$", line.strip())
    if match:
      timestamp = match.group(1)
      name = match.group(2).strip()
      tracks.append({"name": name, "start": timestamp})

  with open(tracklistFile, "w") as f:
    json.dump({
      "artistName": artistName,
      "albumName": albumName,
      "albumYear": albumYear,
      "tracks": tracks
    }, f, indent=2)

  print(f"Saved {len(tracks)} tracks to tracklist.json\n")

def printInputData():
  with open(tracklistFile, "r") as f:
    data = json.load(f)
  print(json.dumps(data, indent=2))