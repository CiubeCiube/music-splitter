# Music Splitter

A CLI utility to split a single audio file into individual tracks using a JSON tracklist

- Tested with Python 3.12.4
- **Requires Python 3.12** — pydub is not compatible with Python 3.13+

| Required Packages |
|---|
| pydub |
| mutagen |

| System Dependencies |
|---|
| ffmpeg |

---

### Supported formats

| Input | Output |
|---|---|
| .mp3 | .mp3 |
| .m4a | .m4a |
| .flac / other | .flac |

---

### Usage

Place the source audio file and the `tracklist.json` file inside the `data/` folder, then run:

```bash
python main.py
```

---

### Available actions

| Option | Description |
|---|---|
| 1 | Enter tracks data interactively and populate `tracklist.json` |
| 2 | Preview tracklist and split the audio file |
| 0 | Exit |

---

### Tracklist format

When entering tracks, paste each track on its own line using this format:

```
[mm:ss] Track Name
[h:mm:ss] Track Name
```

Example:

```
[0:01] Mythologies
[3:16] One More Time
[1:01:00] Turn On The Lights again..
```

Press Enter twice when done.

---

### tracklist.json structure

```json
{
  "artistName": "Artist Name",
  "albumName": "Album Name",
  "albumYear": "2026",
  "tracks": [
    {
      "name": "Track Name",
      "start": "0:01"
    }
  ]
}
```

---

### Output

Split tracks are saved in the `output/` folder, created automatically. Each file is named as:

```
01. Track Name.m4a
02. Track Name.m4a
```

Each file is exported with the following metadata: title, artist, album, track number, and year.