# VideoMaker Helper

Micro tools for content creators!


## Install

`pipx install git+https://github.com/dunossauro/videomaker-helper.git`


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

### `cut-video`

The `cut-video` command offers content creators a streamlined way to automatically edit videos based on silence detection. By analyzing the audio content within the video, this function trims away portions of the video deemed as "silence", making it particularly useful for removing unintended pauses, long gaps, or any unwanted quiet segments.

#### Features:

- **Input Options**: This command takes a video file as its primary input. An additional audio file can also be provided if desired.

- **Automatic Editing**: By leveraging silence detection, the video can be automatically edited without the need for manual intervention.

- **Customizable Parameters**: Users can fine-tune the editing process using several parameters:
  - `silence-time`: Specifies the minimum duration of silence (in milliseconds) that should be considered for trimming.
  - `threshold`: Sets the decibel level to detect silence in the audio.
  - `distance`: Choose the gap between the silences. Options range from short to sec.
  - `codec`: Specifies the codec to be used when generating the edited video.

- **Default Output**: If no `output_path` is provided, the edited video will be saved as `result.mp4`.

#### Example Usage:

To edit a video named `sample.mp4` using default parameters, use:

```
vmh cut-video sample.mp4
```

#### `--help` Flag Output:

The following provides an overview of the available options and arguments for the `cut-video` command:

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


### `Transcribe`

The `transcribe` command is a powerful tool designed to convert audio content from video or standalone audio files into readable text, producing subtitles for the given content.

- **Input Types**: This command can process both video and audio files.

- **Output Modes**: With the `--mode` flag, users can specify the desired output format for the transcriptions:
  - `txt`: Produces a `.txt` file with the transcription.
  - `json`: Generates a structured `.json` file containing the transcription data.
  - `srt`: Creates a `.srt` subtitle file, commonly used with video players.
  - `print`: Instead of saving to a file, this mode displays the transcription result directly in the console.

- **Optional Output Path**: While you can specify an `output_path` to determine where the generated file (txt, json, or srt) will be saved, it's not mandatory. If not provided, the default filename will be `output.srt`.

Example Usage:

To transcribe an audio file named `audio.mp3` and get the transcription result in a JSON format, use:

```
vmh transcribe audio.mp3 --mode json
```

`--help` Flag Output:

The following shows the output you'd receive when using the `--help` flag with the `transcribe` command:

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
