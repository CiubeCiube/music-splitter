import json
import re

from files import tracklistFile

def msTime(time):
  timeStr = f"{time:.2f}"
  parts = timeStr.split(".")
  minutes = int(parts[0])
  seconds = int(parts[1])
  return (minutes * 60 + seconds) * 1000

def populateConfig():
  artistName = input("Artist Name: ")
  albumName = input("Album Name: ")
  albumYear = input("Album Year: ")
  tracksInput = input("Tracks: ")

  pattern = r"(\d+\.\d+)\s+(.+?)(?=\s+\d+\.\d+|$)"
  matches = re.findall(pattern, tracksInput.strip())

  tracks = [
    {"name": title.strip(), "start": float(timestamp)}
    for timestamp, title in matches
  ]

  json.dump({
    "artistName": artistName,
    "albumName": albumName,
    "albumYear": albumYear,
    "tracks": tracks
  }, tracklistFile)

def printInputData():
  with open("./data/tracklist.json", "r") as f:
    data = json.load(f)
  print(json.dumps(data, indent=2))