# VideoMaker Helper

VideoMaker Helper is a collection of command-line utilities designed to simplify common tasks for video and audio content creators. These tools aim to automate specific aspects of the video-making process, reducing manual work and enhancing overall efficiency.

## Core Features:

- **Silence Detection**: Automatically detect silent segments in audio files. Useful for determining parts to edit or skip.

- **Audio Equalization**: Adjust the audio to a consistent level across a file. This tool can add compression and gain to improve the listening experience.

- **Audio Extraction**: Pull audio content from video files. With an option to receive both the raw extracted audio and an equalized version.

- **Video Editing**: Based on silence detection, automatically cut portions of a video, providing a streamlined content experience.

## Installation:

To install VideoMaker Helper, simply use the following command:

```bash
pipx install git+https://github.com/dunossauro/videomaker-helper.git
```

With VideoMaker Helper installed, you can easily run any of the included tools from your terminal. It's a practical toolset for anyone looking to expedite their content creation process.


## Tools

VideoMaker Helper comes with an array of specialized utilities tailored for video and audio content editing. These tools have been crafted keeping the needs of content creators in mind, ensuring each task is done with precision while saving valuable time.

### `extract-audio`

The `extract-audio` command is designed to detach the audio component from a video file. Whether you're repurposing the audio content of videos for podcasts, transcription, or other audio-centric endeavors, this tool provides a seamless experience.

#### Features:

- **Dual Audio Extraction with `--eq` Flag**: 
  - When you use the `--eq` flag, the command produces two distinct audio files:
    1. A pure audio file extracted directly from the video.
    2. An enhanced audio file where compression is applied, and the volume is amplified by 10 decibels.
  - This gives users the flexibility to have both the raw and enhanced versions for various applications.

- **Default Output**: If an `output_file` isn't specified, the extracted audio will default to `output.wav`. If `--eq` is used, the enhanced version might have a suffix or different naming to differentiate it from the raw audio.

- **Opt-Out of Audio Enhancement**: If you only want the raw, unaltered audio without the enhanced version, simply use the `--no-eq` flag.

#### Example Usage:

To extract both raw and enhanced audio from a video named `presentation.mp4`:

```
vmh extract-audio presentation.mp4 --eq
```

For raw audio extraction without any enhancement:

```
vmh extract-audio presentation.mp4 --no-eq
```

#### `--help` Flag Output:

For a detailed breakdown of the available options and arguments for the `extract-audio` command:

```
vmh extract-audio --help

 Usage: vmh extract-audio [OPTIONS] AUDIO_FILE [OUTPUT_FILE]

 Extracts the audio from a video.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH           [default: None] [required]              │
│      output_file      [OUTPUT_FILE]  [default: output.wav]                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --eq      --no-eq      Add compression and 10db of extracted audio           │
│                        [default: eq]                                         │
│ --help                 Show this message and exit.                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### `silences`

**Command Purpose**: The `silences` command is primarily designed for analyzing audio files to detect silent portions. Such functionality is invaluable for content creators, sound engineers, and anyone else needing to identify and potentially edit the silent intervals within their audio assets.

#### Main Features:

- **Efficient Caching System**: If an audio file has already been scrutinized using the `silences` command, the results are stored in a cache. When the same file is subjected to another silence check, the command fetches and returns the cached results rather than re-analyzing the entire file. This ensures quicker results and reduced computational overhead.

- **Bypassing Cache with `--force` Option**: In situations where the audio file might have undergone changes and needs a fresh evaluation, the `--force` flag can be used to bypass the cache and conduct a new analysis.

- **Customizable Silence Detection**: The command offers multiple parameters to finetune silence detection:
  - `--silence-time`: Designates the minimum duration, in milliseconds, to be categorized as silence.
  - `--threshold`: Specifies the decibel threshold to determine silence.
  - `--distance`: Enables users to set the precision of silence detection — be it short, mid, long, or exact (sec) intervals.

#### Sample Commands:

1. For identifying silent segments in an audio file named `music.wav`:
```
vmh silences music.wav
```

2. To conduct a new evaluation, overriding cached results:
```
vmh silences music.wav --force
```

#### `--help` Option Display:

For a comprehensive list of available options and arguments for the `silences` command:

```
vmh silences --help
 Usage: vmh silences [OPTIONS] AUDIO_FILE...

 Checks for silences in an audio file.
 The checks are cached, so if the file has already been analyzed, it will return the
 cache.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    audio_file      AUDIO_FILE...  [default: None] [required]                          │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --silence-time                  INTEGER               Minimal time in ms for configure  │
│                                                       a silence                         │
│                                                       [default: 400]                    │
│ --threshold                     INTEGER               Value in db for detect silence    │
│                                                       [default: -65]                    │
│ --distance                      [short|mid|long|sec]  [default: Distance.short]         │
│ --force           --no-force                          Ignore cache [default: no-force]  │
│ --help                                                Show this message and exit.       │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Advanced Command Sample:

Suppose you have an audio file, `<audio_path>`, and you want to identify silent segments with a stricter definition of silence. For this, you might want the silent interval to be at least half a second (500 milliseconds) long, and the sound level to be below -30 decibels to be considered silent.

You can achieve this advanced silence detection using the command:

```
vmh silences <audio_path> --silence-time 500 --threshold -30
```

#### Explanation:

- `--silence-time 500`: This option sets the minimal duration for a segment to be recognized as silence to 500 milliseconds. Any quiet interval shorter than this will not be flagged.

- `--threshold -30`: With this option, any segment of the audio that falls below -30 decibels will be categorized as silent. This is a higher threshold compared to the default of -65 decibels, implying a stricter definition of what is considered silent.

Using these parameters, the command will return only those portions of `<audio_path>` that are both longer than 500 milliseconds and quieter than -30 decibels, allowing for a more specific and refined detection of silent segments.


### `cut-silences`

The `cut-silences` command is an essential utility for audio editors, podcasters, and content creators who wish to refine the auditory experience of their content. It meticulously scans the provided audio file and removes all the detected silent portions, ensuring the end result is a continuous and engaging audio piece without abrupt or prolonged gaps.

#### Features:

- **Simple Input**: The command needs just the source `audio_file` and the desired `output_file` where the processed audio will be saved.

- **Efficient Silence Removal**: Leveraging advanced algorithms, this tool efficiently detects and eliminates silences, making the audio flow more natural.

- **Customizable Detection**: Users have the flexibility to define what constitutes a 'silence' in their audio:
  - `silence-time`: Determines the minimum duration of a silence (measured in milliseconds) before it's considered for removal.
  - `threshold`: Sets the decibel level below which an audio segment is considered silent.

#### Example Usage:

To remove silences from an audio file named `podcast.mp3` and save the processed audio as `podcast_no_silences.mp3`, use:

```
vmh cut-silences podcast.mp3 podcast_no_silences.mp3
```

#### `--help` Flag Output:

For those seeking a quick reference of available options and arguments for the `cut-silences` command:

```
vmh cut-silences --help

 Usage: vmh cut-silences [OPTIONS] AUDIO_FILE OUTPUT_FILE

 Removes all silences from an audio file.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH  [default: None] [required]                       │
│ *    output_file      PATH  [default: None] [required]                       │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --silence-time        INTEGER  Minimal time in ms for configure a silence    │
│                                [default: 400]                                │
│ --threshold           INTEGER  Value in db for detect silence [default: -65] │
│ --help                         Show this message and exit.                   │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### `equalize`

The `equalize` command serves as an audio enhancer, providing users the ability to infuse both compression and gain into their audio files. Whether you're refining a podcast, optimizing an interview recording, or leveling the audio of a music track, this tool offers a quick and efficient way to elevate the quality of the sound output.

#### Features:

- **Audio Enhancement**: The primary purpose of the command is to improve audio clarity by automatically applying compression and amplifying the gain, making the audio more consistent and pleasant to the ears.

- **Default Output**: If an `output_file` is not specified, the processed audio is saved as `output.wav` by default.

- **Adjustable Gain**: With the `--gain` option, users can customize the amount of decibel increase they want to apply to the audio.

#### Example Usage:

To equalize an audio file named `interview.mp3` and enhance its gain by 15 decibels, use:

```
vmh equalize interview.mp3 --gain 15
```

#### `--help` Flag Output:

For those seeking a comprehensive overview of available options and arguments for the `equalize` command:

```
vmh equalize --help

 Usage: vmh equalize [OPTIONS] AUDIO_FILE [OUTPUT_FILE]

 Add Compression and Gain for audio file.

╭─ Arguments ──────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH           [default: None] [required]              │
│      output_file      [OUTPUT_FILE]  [default: output.wav]                   │
╰──────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────╮
│ --gain        INTEGER  Add dbs in audio [default: 10]                        │
│ --help                 Show this message and exit.                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### `kdenlive`

> ⚠ Instable interface

TODO doc


```
vmh kdenlive --help

 Usage: vmh kdenlive [OPTIONS] AUDIO_FILE VIDEO_FILE INPUT_XML [OUTPUT_PATH]

 Generates an XML compatible with kdenlive settings.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH           [default: None] [required]                         │
│ *    video_file       PATH           [default: None] [required]                         │
│ *    input_xml        PATH           [default: None] [required]                         │
│      output_path      [OUTPUT_PATH]  [default: timelines]                               │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────╯
```

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

## Distance Flag

The `distance` flag is an integral aspect of the VMH's tools, providing users with the ability to adjust the "padding" or extra duration added to the silence sections, thereby refining the cut points in the audio or video. This is especially critical when relying on silence durations as a guiding metric for edits. By adjusting the distance, you can prevent abrupt truncations and allow for smoother transitions, ensuring that the content feels more natural even after cuts.

### Options:

The `distance` flag offers four distinct options, represented in the `Distance` Enum:

```python
class Distance(str, Enum):
    short = 'short'
    mid = 'mid'
    long = 'long'
    sec = 'sec'
```

Each option corresponds to a specific padding duration, as outlined in the `threshold_distance` dictionary:

```python
threshold_distance = {'short': 0.100, 'mid': 0.250, 'long': 0.500, 'sec': 1}
```

Here's a breakdown of each option:

- **short**: Adds a padding of 0.100 seconds (or 100 milliseconds) to the detected silences.
- **mid**: Introduces a more noticeable padding of 0.250 seconds (or 250 milliseconds).
- **long**: Provides an even longer padding, extending the silence by 0.500 seconds (or 500 milliseconds).
- **sec**: Offers the most extended padding option, adding a full second (1 second) to the silences.


### Practical Implications:

By default, using silences as the sole guide for cuts can occasionally result in the "truncation" of segments, making the content appear abruptly cut. Increasing the distance ensures the cuts are more fluid and seamless. 

However, a trade-off exists. As you increase the distance, the final content might become lengthier, but it offers a smoother, more polished finish. On the other hand, shorter distances might lead to a more concise output but at the risk of it seeming abruptly edited.

In essence, the right choice of distance will depend on the nature of the content, the target audience, and the desired final product's length and feel. It's a balance between conciseness and fluidity.

## Cache system
TODO doc

## Future Vision

VideoMaker Helper is continually evolving, built with the aim to be an indispensable tool for content creators. As we look ahead, there are several enhancements and features that we dream of incorporating into the tool. Here's a glimpse into the exciting roadmap we envision for VideoMaker Helper:

### Package Distribution
- **Publish Package**: In our ongoing efforts to make VideoMaker Helper accessible to everyone, we plan to publish the package for easier installation and updates. This will streamline the user experience, ensuring that the tool is just a command away.

### Advanced Audio Enhancements
- **VST3 and Lv2 Support for Equalization**: Our goal is to provide users with advanced audio processing capabilities. By integrating VST3 and Lv2 support, VideoMaker Helper will offer a wider array of audio effects and enhancements, ensuring top-notch audio output.

- **Extract Multi-channel Audio**: We recognize the growing demand for multi-channel audio extraction. Soon, VideoMaker Helper will be equipped to extract 5.1 and 7.1 audio into separate files, catering to professional audio processing needs.

### Seamless Video Editing Integration
- **Transparent `kdenlive` Command**: Our vision extends to creating a tool that works seamlessly with popular video editing software. The plan is to refine the `kdenlive` command, making it not just transparent but also incredibly useful for users.

- **Support Other Video Editors with OTIO**: Recognizing the diverse tools content creators employ, we aim to support various video editors by leveraging OpenTimelineIO (OTIO). This will expand the horizons of VideoMaker Helper, making it a universally compatible tool.

## Powered by Python: Project Dependencies

VideoMaker Helper is a testament to the dynamic capabilities of the Python ecosystem. Crafted with passion in Brazil, this CLI stands tall on the shoulders of some exceptional Python projects. Here are the primary libraries and frameworks that make VideoMaker Helper tick:

- **[pydub](https://github.com/jiaaro/pydub)**: An intuitive library that simplifies audio processing, allowing us to manipulate and analyze sound effortlessly.

- **[moviepy](https://github.com/Zulko/moviepy)**: A versatile tool that empowers us to edit videos with a Pythonic touch, making complex video manipulations a breeze.

- **[Whisper](https://openai.com/research/publications/whisper-an-automatic-speech-recognition-system-for-conversational-speech/)**: OpenAI's automatic speech recognition (ASR) system. It's designed to convert spoken language into written text, making audio transcription efficient and accurate.

- **[pedalboard](https://github.com/spotify/pedalboard)**: Developed by Spotify, this library provides a robust platform for audio effects, further enhancing the audio capabilities of VideoMaker Helper.

These dependencies, among others, form the backbone of our tool, and we express our deepest gratitude to the developers and communities behind these projects. Their commitment to open-source innovation drives tools like VideoMaker Helper to push boundaries and redefine content creation.
