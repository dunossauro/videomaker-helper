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
```
vmh cut-video --help

 Usage: vmh cut-video [OPTIONS] VIDEO_FILE [AUDIO_FILE] [OUTPUT_PATH]

 Edits a video using silences as reference.

╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    video_file       PATH           [default: None] [required]                                                       │
│      audio_file       [AUDIO_FILE]                                                                                    │
│      output_path      [OUTPUT_PATH]  [default: result.mp4]                                                            │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --silence-time        INTEGER                                        Minimal time in ms for configure a silence       │
│                                                                      [default: 400]                                   │
│ --threshold           INTEGER                                        Value in db for detect silence [default: -65]    │
│ --distance            [short|mid|long|sec]                           [default: Distance.short]                        │
│ --codec               [libx264|mpeg4|rawvideo|png|libvorbis|libvpx]  [default: Codec.mpeg4]                           │
│ --help                                                               Show this message and exit.                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### transcribe

```
vmh transcribe --help

 Usage: vmh transcribe [OPTIONS] AUDIO_PATH [OUTPUT_PATH]

 Transcribes an audio file into subtitles.

╭─ Arguments ───────────────────────────────────────────────────────────────────────╮
│ *    audio_path       PATH           [default: None] [required]                   │
│      output_path      [OUTPUT_PATH]  [default: output.srt]                        │
╰───────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────────────────────────────────────╮
│ --mode        [print|txt|json|srt]  [default: TranscribeModes.srt]                │
│ --help                              Show this message and exit.                   │
╰───────────────────────────────────────────────────────────────────────────────────╯
```


### Usage

```bash
vmh --help

Usage: vmh [OPTIONS] COMMAND [ARGS]...

╭─ Commands ────────────────────────────────────────────────────────────────────────╮
│ cache              Cache tools.                                                   │
│ cut-silences       Removes all silences from an audio file.                       │
│ cut-video          Edits a video using silences as reference.                     │
│ equalize           Adds compression and 10db gain.                                │
│ extract-audio      Extracts the audio from a video.                               │
│ grammar-check      Check grammar in a tex tfile.                                  │
│ kdenlive           Generates an XML compatible with kdenlive settings.            │
│ silences           Checks for silences in a audio file.                           │
│ transcribe         Transcribes an audio file into subtitles.                      │
╰───────────────────────────────────────────────────────────────────────────────────╯
```
