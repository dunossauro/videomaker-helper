The `extract-audio` command is designed to detach the audio component from a video file. Whether you're repurposing the audio content of videos for podcasts, transcription, or other audio-centric endeavors, this tool provides a seamless experience.

## Features:

- **Dual Audio Extraction with `--eq` Flag**: 
  - When you use the `--eq` flag, the command produces two distinct audio files:
    1. A pure audio file extracted directly from the video.
    2. An enhanced audio file where compression is applied, and the volume is amplified by 10 decibels.
  - This gives users the flexibility to have both the raw and enhanced versions for various applications.

- **Default Output**: If an `output_file` isn't specified, the extracted audio will default to `output.wav`. If `--eq` is used, the enhanced version might have a suffix or different naming to differentiate it from the raw audio.

- **Opt-Out of Audio Enhancement**: If you only want the raw, unaltered audio without the enhanced version, simply use the `--no-eq` flag.

## Example Usage:

To extract both raw and enhanced audio from a video named `presentation.mp4`:

```
vmh extract-audio presentation.mp4 --eq
```

For raw audio extraction without any enhancement:

```
vmh extract-audio presentation.mp4 --no-eq
```

## `--help` Flag Output:

For a detailed breakdown of the available options and arguments for the `extract-audio` command:

```
vmh extract-audio --help

 Usage: vmh extract-audio [OPTIONS] VIDEO_FILE [OUTPUT_FILE]

 Extracts the audio from a video.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    video_file       PATH           [default: None] [required]              │
│      output_file      [OUTPUT_FILE]  [default: output.wav]                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --eq      --no-eq      Add compression and 10db of extracted audio           │
│                        [default: eq]                                         │
│ --help                 Show this message and exit.                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## API for developers

::: videomaker_helper.audio.extract_audio
