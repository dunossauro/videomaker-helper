# Cut Silences

The `cut-silences` command is an essential utility for audio editors, podcasters, and content creators who wish to refine the auditory experience of their content. It meticulously scans the provided audio file and removes all the detected silent portions, ensuring the end result is a continuous and engaging audio piece without abrupt or prolonged gaps.


## Features:

- **Simple Input**: The command needs just the source `audio_file` and the desired `output_file` where the processed audio will be saved.

- **Efficient Silence Removal**: Leveraging advanced algorithms, this tool efficiently detects and eliminates silences, making the audio flow more natural.

- **Customizable Detection**: Users have the flexibility to define what constitutes a 'silence' in their audio:
  - `silence-time` (or `-s`): Determines the minimum duration of a silence (measured in milliseconds) before it's considered for removal.
  - `threshold` (or `-t`): Sets the decibel level below which an audio segment is considered silent.


## Example Usage:

To remove silences from an audio file named `podcast.mp3` and save the processed audio as `podcast_no_silences.mp3`, use:

```
vmh cut-silences podcast.mp3 podcast_no_silences.mp3
```

### `--help` Flag Output:

```console exec="1" source="console" result="ansi"
$ vmh cut-silences --help
```


## API for developers

::: videomaker_helper.audio.cut_silences

