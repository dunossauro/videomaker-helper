# VideoMaker Helper

Micro tools for content creators!


## Install

`pipx install https://github.com/dunossauro/videomaker-helper.git`


## Tools

### extract-audio

Extracts the audio from a video file.

Usage:

`vmh extract-audio <audio_path>`

### silences

Detect silences in an audio file and save in cache

Basic usage:

`vmh silences <audio_path>`

Advanced usage:

`vmh silences <audio_path> --silence-time 500 --threshold -30`


### cut-silences

Cut an audio file using silences

### equilize

TODO doc

### kdenlive

TODO doc

### cut-video

Create a new video with silences cuted

Only video:
`vmh cut-video <video_file> <output_path>`

Vídeo with external audio:
`vmh cut-video <video_file> <audio_path> <output_path>`

### transcribe

Transcribes an audio file into subtitles.

Usage:
`vmh transcribe <audio_path>`


### Usage

```bash
vmh --help

Usage: vmh [OPTIONS] COMMAND [ARGS]...

╭─ Commands ──────────────────────────────────────────────────────────────────╮
│ cache                  Cache tools.                                         │
│ cut-silences           Removes all silences from an audio file.             │
│ cut-video              Edits a video using silences as reference.           │
│ equalize               Adds compression and 10db gain.                      │
│ extract-audio          Extracts the audio from a video.                     │
│ grammar-check          Check grammar in a tex tfile.                        │
│ kdenlive               Generates an XML compatible with kdenlive settings.  │
│ silences               Checks for silences in a audio file.                 │
│ transcribe             Transcribes an audio file into subtitles.            │
╰─────────────────────────────────────────────────────────────────────────────╯
```
