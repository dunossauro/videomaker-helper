# 📹 VideoMaker Helper

VideoMaker Helper is a collection of command-line utilities designed to simplify common tasks for video and audio content creators. These tools aim to automate specific aspects of the video-making process, reducing manual work and enhancing overall efficiency.

## 🥝 Core Features:

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


## ⚒️Tools

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

- **Tailored Silence Detection**: Users are empowered to adapt the silence detection criteria using various parameters:
  - `--silence-time` (or `-s`): Defines the minimal duration, in milliseconds, required for an interval to be classified as silence.
  - `--threshold` (or `-t`): Determines the decibel threshold that demarcates silent portions.
  - `--distance` (or `-d`): Helps in stipulating how silences are grouped, with options ranging from short to exact (sec) intervals.

#### Sample Commands:

1. For identifying silent segments in an audio file named `music.wav`:
```
vmh silences music.wav
```

2. To conduct a new evaluation, overriding cached results:
```
vmh silences music.wav --force
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

#### `--help` Option Display:

For a comprehensive list of available options and arguments for the `silences` command:

```
vmh silences --help

 Usage: vmh silences [OPTIONS] AUDIO_FILE...

 Checks for silences in a audio file.
 The checks are cached, so if the file has already been analyzed, it will return the cache.

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    audio_file      AUDIO_FILE...  [default: None] [required]                                                     │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --silence-time  -s                INTEGER               Minimal time in ms for configure a silence [default: 400]  │
│ --threshold     -t                INTEGER               Value in db for detect silence [default: -65]              │
│ --distance      -d                [short|mid|long|sec]  Distance betweet silences [default: Distance.short]        │
│ --force             --no-force                          Ignore cache [default: no-force]                           │
│ --help                                                  Show this message and exit.                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

### `cut-silences`

The `cut-silences` command is an essential utility for audio editors, podcasters, and content creators who wish to refine the auditory experience of their content. It meticulously scans the provided audio file and removes all the detected silent portions, ensuring the end result is a continuous and engaging audio piece without abrupt or prolonged gaps.

#### Features:

- **Simple Input**: The command needs just the source `audio_file` and the desired `output_file` where the processed audio will be saved.

- **Efficient Silence Removal**: Leveraging advanced algorithms, this tool efficiently detects and eliminates silences, making the audio flow more natural.

- **Customizable Detection**: Users have the flexibility to define what constitutes a 'silence' in their audio:
  - `silence-time` (or `-s`): Determines the minimum duration of a silence (measured in milliseconds) before it's considered for removal.
  - `threshold` (or `-t`): Sets the decibel level below which an audio segment is considered silent.

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

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH  [default: None] [required]                                       │
│ *    output_file      PATH  [default: None] [required]                                       │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
│ --silence-time  -s      INTEGER  Minimal time in ms for configure a silence [default: 400]   │
│ --threshold     -t      INTEGER  Value in db for detect silence [default: -65]               │
│ --help                           Show this message and exit.                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────╯
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

**Command Purpose**: The `kdenlive` command facilitates video editors by generating XML files compatible with kdenlive settings, focusing specifically on automating the process of cutting silences from video timelines. This utility is especially designed to expedite the editing workflow, allowing users to jumpstart their projects with silences already trimmed, effectively eliminating one of the most time-consuming and tedious aspects of video editing.

> ⚠️ **Instability Alert**: The interface for the `kdenlive` command is currently unstable. Users should anticipate potential modifications in future updates.

#### Main Features:

- **Automatic Silence-Cut Generation**: VMH harnesses the `silences` command's capabilities to detect silent portions in your audio file. These detected silences are then converted into kdenlive-compatible XML cut instructions, effectively pre-empting the need for manual audio silence trimming.

- **Efficient XML Creation for Kdenlive**: This command abstracts away the complexities of kdenlive's XML structure. Instead of fumbling with XML details, users can generate the required XML content for their timelines swiftly and effortlessly.

- **Fine-Tuned Silence Detection**: Video editors can customize the silence detection parameters to suit their specific requirements:
  - `--silence-time`: Sets the minimum duration for a segment to be recognized as silence.
  - `--threshold`: Determines the decibel level to qualify a segment as silent.
  - `--distance`: Adjusts the granularity of silence detection, with options from short intervals to exact durations.

- **Manual XML Integration**: For now, this command doesn’t directly alter existing kdenlive XML files. Instead, it generates standalone XML files with the necessary cut instructions. To incorporate these cuts into the main project, users must manually integrate this XML content into their primary kdenlive XML files. Seamless integration is a planned feature for future updates.

#### Sample Commands:

1. For an automated silence-trimmed XML setup using `audio.wav`, `video.mp4`, and `project.xml`:
```
vmh kdenlive audio.wav video.mp4 project.xml
```

2. Customizing silence detection parameters for the XML generation:
```
vmh kdenlive audio.wav video.mp4 project.xml --silence-time 500 --threshold -30
```

#### `--help` Option Display:

A snapshot of available options and arguments for the `kdenlive` command:

```
vmh kdenlive --help

 Usage: vmh kdenlive [OPTIONS] AUDIO_FILE VIDEO_FILE INPUT_XML [OUTPUT_PATH]

 Generates XML tailored to kdenlive settings, emphasizing automated silence cuts.
 Note: It doesn’t directly modify kdenlive files. It creates timeline instructions which you must manually integrate.

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    audio_file       PATH           [default: None] [required]                                          │
│ *    video_file       PATH           [default: None] [required]                                          │
│ *    input_xml        PATH           [default: None] [required]                                          │
│      output_path      [OUTPUT_PATH]  [default: timelines]                                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --silence-time  -s      INTEGER               Minimal time in ms for configure a silence [default: 400]  │
│ --threshold     -t      INTEGER               Value in db for detect silence [default: -65]              │
│ --distance      -d      [short|mid|long|sec]  Distance betweet silences [default: Distance.short]        │
│ --help                                        Show this message and exit.                                │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Integration Instructions:

To weave the XML content generated by the `kdenlive` command into your kdenlive project:

1. Retrieve the produced XML from the designated output path (default: `timelines`).
2. Copy its entire content.
3. Open your primary kdenlive project XML file.
4. Find the section dedicated to timeline data.
5. Manually integrate the copied XML content.
6. Store the changes to the kdenlive project XML file. Open it within the kdenlive software to inspect the implemented trims.

**Coming Soon**: A future update aims to offer direct modifications to the kdenlive XML file, making the integration process smoother and more intuitive.

### `cut-video`

#### Features:

- **Input Options**: This command primarily requires a video file for its operation. Additionally, an optional audio file can be provided if the user wants to use an equalized audio file.

- **Automatic Editing**: Using silence detection, videos are auto-edited, removing the need for manual trims.

- **Customizable Parameters**: The editing process is highly customizable through several parameters:
  - `silence-time`: Designate the minimum duration (in milliseconds) of silence that will be eligible for trimming.
  - `threshold`: Define the decibel level which the tool will use to identify silent sections in the audio.
  - `distance`: Determine the spacing between detected silences. Options include 'short', 'mid', 'long', and 'sec'.
  - `codec`: Designate the codec for rendering the edited video. For an exhaustive list of supported codecs, see [Moviepy specs](https://moviepy.readthedocs.io/en/latest/ref/videotools.html#moviepy.video.tools.credits.CreditsClip.write_videofile).
  - `bitrate`: Designate the video's bitrate. For recommendations on bitrates based on resolutions, refer to the [Youtube table](https://support.google.com/youtube/answer/1722171?hl=en#zippy=%2Cbitrate).

- **Default Output**: In the absence of an `output_path`, the edited video is stored as `result.mp4`.

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

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    video_file       PATH           [default: None] [required]                                                                                            │
│      audio_file       [AUDIO_FILE]   Optional audio equilized audio file                                                                                   │
│      output_path      [OUTPUT_PATH]  [default: result.mp4]                                                                                                 │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --silence-time  -s      INTEGER                                                                 Minimal time in ms for configure a silence [default: 400]  │
│ --threshold     -t      INTEGER                                                                 Value in db for detect silence [default: -65]              │
│ --distance      -d      [short|mid|long|sec]                                                    Distance betweet silences [default: Distance.short]        │
│ --codec         -c      [libx264|mpeg4|rawvideo|png|libvorbis|libvpx]                           [default: Codec.mpeg4]                                     │
│ --preset        -p      [ultrafast|superfast|veryfast|faster|fast|medium|slow|slower|veryslow]  [default: Preset.medium]                                   │
│ --bitrate       -b      TEXT                                                                    [default: 15M]                                             │
│ --help                                                                                          Show this message and exit.                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
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

### `grammar-check`

**Command Purpose**: The `grammar-check` command offers users a powerful utility to analyze text files for grammatical inaccuracies. By harnessing the capabilities of LanguageTool, this command spotlights potential grammatical pitfalls within the text, ensuring textual fidelity and precision.

This tool, though broadly applicable for any textual evaluation, finds its niche within the VMH suite for inspecting generated subtitles. Given the inherent challenges of transcribing speech—like unnatural phrasings, the integration of foreign terms, or hurried articulations—the `grammar-check` ensures that your subtitles not only convey the right message but do so with grammatical accuracy.

#### Main Features:

- **LanguageTool Integration**: Relying on the robust LanguageTool system, the `grammar-check` command evaluates textual content against an extensive database of grammatical rules, pinpointing areas that might benefit from corrections or reconsideration.

- **Tailored for Subtitle Inspection**: While general grammar checks can be performed using this tool, its inclusion within VMH emphasizes its role in auditing subtitles. It becomes instrumental in ensuring that automated transcriptions are not just accurate in content but also in their grammatical construct.

- **Support for Multiple Languages**: The command allows users to specify a language using the `lang` argument, catering to multilingual subtitle generation. By default, it assumes the language to be Brazilian Portuguese (`pt-BR`).

#### Sample Commands:

1. Performing a grammar check on `document.txt` in the default language (Brazilian Portuguese):
```
vmh grammar-check document.txt
```

2. Conducting a grammar check for content in English:
```
vmh grammar-check document.txt en-US
```

#### `--help` Option Display:

A brief overview of available options and arguments for the `grammar-check` command:

```
vmh grammar-check --help

Usage: vmh grammar-check [OPTIONS] FILE [LANG]

  Check grammar in a text file using LanguageTool.

╭─ Arguments ────────────────────────────────────────────────╮
│ *    file      PATH    [default: None] [required]          │
│      lang      [LANG]  [default: pt-BR]                    │
╰────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────╮
│ --help          Display this help message.                 │
╰────────────────────────────────────────────────────────────╯
```

#### Usage Tips:

1. **Consider the Context**: While automated grammar checks are a boon, it's essential to remember that subtleties in speech, especially in transcriptions or subtitles, might lead to flagged areas that are contextually accurate. Always review the suggestions with the context in mind.

2. **Foreign Terms and Phrases**: If your subtitles or text include terms or phrases from different languages, anticipate potential flags from the grammar-check, especially if the specified language for checking is different.

3. **Regular Audits**: For long projects with vast subtitle files, consider periodic grammar checks. This will not only help maintain the quality of your content but also ensure that any corrections can be integrated without revisiting large portions of your work.

### All options

TODO doc

```
vmh

  Usage: vmh [OPTIONS] COMMAND [ARGS]...

  Videomaker Helper!

  ╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────╮
  │ --version             -v                                       Show VMH version                       │
  │ --install-completion          [bash|zsh|fish|powershell|pwsh]  Install completion for the specified   │
  │                                                                shell.                                 │
  │                                                                [default: None]                        │
  │ --show-completion             [bash|zsh|fish|powershell|pwsh]  Show completion for the specified      │
  │                                                                shell, to copy it or customize the     │
  │                                                                installation.                          │
  │                                                                [default: None]                        │
  │ --help                                                         Show this message and exit.            │
  ╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯
  ╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────╮
  │ cache                  Cache tools.                                                                   │
  │ cut-silences           Removes all silences from an audio file.                                       │
  │ cut-video              Edits a video using silences as reference.                                     │
  │ equalize               Add Compression and Gain dor audio file.                                       │
  │ extract-audio          Extracts the audio from a video.                                               │
  │ grammar-check          Check grammar in a tex tfile.                                                  │
  │ kdenlive               Generates an XML compatible with kdenlive settings.                            │
  │ silences               Checks for silences in a audio file.                                           │
  │ transcribe             Transcribes an audio file into subtitles.                                      │
  ╰───────────────────────────────────────────────────────────────────────────────────────────────────────╯
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

## Understanding Audio Threshold and Silence Duration

To use VideoMaker Helper effectively, it's essential to understand two key parameters: **Audio Threshold** and **Silence Duration**. These parameters determine which parts of an audio track are considered speech (and therefore kept) and which are regarded as silence or noise (and hence removed).

### Audio Waveform

Imagine your audio as a line graph:
- The vertical axis represents volume (loudness).
- The horizontal axis represents time.

When you speak or make a sound, the line (or waveform) rises and falls, representing the loudness of that sound over time.

### Threshold

The **threshold** is like a horizontal line on this graph, set at a specific volume level. Here's how it works:
- Any sound louder than this line is considered "audio" that we want to keep.
- Any sound quieter than this line is a potential candidate for removal.

By default, the threshold is often set at -65 dBs. However, based on the recording environment and specific requirements, you might need to adjust this level. For instance, in a noisy environment, the threshold might need to be higher.

### Silence Duration

Even if the sound dips below our threshold, it doesn't automatically qualify for removal. This is where **silence duration** comes into play. Here's the breakdown:
- It specifies how long the sound must be below the threshold before being considered "true silence."
- For instance, with a default of 400ms, any quiet moment below the threshold that's shorter than 400ms will be retained. This ensures we don't remove natural pauses in speech.

### How to Choose What to Keep and What to Cut

With these two parameters in place:
1. Audio louder than the threshold is always retained.
2. Audio quieter than the threshold gets removed only if its duration exceeds the specified silence duration.

This approach ensures the final audio sounds as natural as possible, without unnecessary noise or lengthy silences. 

### Practical Application

When using VideoMaker Helper commands, you'll often see parameters like `--threshold` or `--silence-time`. These directly relate to the principles discussed above. Adjusting them allows you to tailor the audio processing to your specific needs.

For instance, the `vmh kdenlive` command offers the ability to adjust the threshold and silence duration, allowing for customized audio trimming based on the user's preferences.

---

With a clear understanding of these principles, you'll be better equipped to use VideoMaker Helper to its full potential, ensuring your videos have crisp, clean audio that's free of distracting silences or noise.

## Cache system
TODO doc

## Future Vision

VideoMaker Helper is continually evolving, built with the aim to be an indispensable tool for content creators. As we look ahead, there are several enhancements and features that we dream of incorporating into the tool. Here's a glimpse into the exciting roadmap we envision for VideoMaker Helper:

### Package Distribution
- **Publish Package**: In our ongoing efforts to make VideoMaker Helper accessible to everyone, we plan to publish the package for easier installation and updates. This will streamline the user experience, ensuring that the tool is just a command away.

### Advanced Audio Enhancements
- **Equalize System Overhaul**: Our aspiration is to magnify the capabilities of our equalize system. With the integration of [librosa](https://librosa.org/doc/latest/index.html#), we aim to detect volume disparities within audio files to engineer a crisp and harmonious audio output. The resultant audio will gracefully dance between -9 and -6 dB, striking a perfect balance between clarity and intensity.

- **VST3 and Lv2 Support for Equalization**: Our goal is to provide users with advanced audio processing capabilities. By integrating VST3 and Lv2 support, VideoMaker Helper will offer a wider array of audio effects and enhancements, ensuring top-notch audio output.

- **Extract Multi-channel Audio**: We recognize the growing demand for multi-channel audio extraction. Soon, VideoMaker Helper will be equipped to extract 5.1 and 7.1 audio into separate files, catering to professional audio processing needs.

### Seamless Video Editing Integration
- **Transparent `kdenlive` Command**: Our vision extends to creating a tool that works seamlessly with popular video editing software. The plan is to refine the `kdenlive` command, making it not just transparent but also incredibly useful for users.

- **Support Other Video Editors with OTIO**: Recognizing the diverse tools content creators employ, we aim to support various video editors by leveraging OpenTimelineIO (OTIO). This will expand the horizons of VideoMaker Helper, making it a universally compatible tool.

With every envisioned enhancement, our foremost commitment remains to empower content creators, enabling them to weave stories with finesse, clarity, and flair. Your feedback, as always, remains instrumental in shaping the trajectory of VideoMaker Helper.

### Comprehensive Documentation and Accessibility
- **Full Project Documentation**: Recognizing the necessity for clear and detailed guidelines, our roadmap involves developing a comprehensive documentation for VideoMaker Helper. From installation to intricate functionalities, every aspect of the tool will be meticulously detailed, ensuring users have a seamless experience.

- **Mkdocs Deployment**: To further elevate the accessibility and user experience, we plan to deploy our documentation using `mkdocs`. With its responsive design and interactive features, this will enable users to easily navigate, search, and explore the various facets of VideoMaker Helper. The documentation will be regularly updated, ensuring it remains in tandem with the tool's evolutions.

Guided by our commitment to serve the community, we endeavor to make VideoMaker Helper not just a tool but a companion for content creators. As we forge ahead, we continually seek feedback and suggestions, ensuring our tool resonates with the evolving needs of our users.

Certainly! Extensive testing is a cornerstone for ensuring software reliability and trustworthiness. Let's add that to the "Future Vision" section:

### Robust Testing for Reliability
- **Comprehensive Testing Suite**: As VideoMaker Helper continues to grow and evolve, we understand the paramount importance of ensuring its stability and reliability. Our vision includes developing an exhaustive suite of tests that cover every conceivable scenario, functionality, and edge case. This will not only provide a safeguard against potential issues but will also serve as a testament to our commitment to quality.

- **Continuous Integration and Delivery (CI/CD)**: Beyond just developing tests, we aim to implement a robust CI/CD pipeline. This will ensure that every update or addition to the tool undergoes rigorous testing before it reaches our users. This approach guarantees that the tool remains bug-free and operates at its optimal level at all times.

- **Feedback-Driven Testing**: We believe in the power of community feedback. We plan to incorporate a system that allows users to report issues and suggest test scenarios. This community-driven approach will further bolster our testing efforts, ensuring the tool is vetted from multiple perspectives.

By placing a strong emphasis on testing, we aim to provide our users with a tool that they can trust implicitly, knowing that it's been rigorously vetted and refined to offer a seamless experience.

### User-Focused Configurations
- **Global Parameter Configuration**: We recognize that different creators have unique preferences and production setups. With that in mind, we envision introducing a global configuration system. This will allow users to set default parameters for aspects like "distance", "threshold", and "silence-time", streamlining the command execution process. This means, rather than repeatedly entering their preferred parameters for each command, users can set them once and have the system use those defaults for all subsequent actions.

- **Config Command**: To facilitate this, the implementation will likely introduce a `config` command. This will be the gateway for users to set, modify, or view their global preferences.

- **Storage with Appdirs**: By utilizing "appdirs", we plan to ensure that the configurations are stored in appropriate, OS-specific directories. This ensures compatibility, organization, and ease of access.

- **Use of TOML Format**: Embracing the clarity and human-friendliness of TOML, the configuration settings will be saved in this format. This ensures that, if users need to manually inspect or modify the configuration file, they are met with a format that's intuitive and easy to understand.

Incorporating this user-focused configuration system is our way of personalizing VideoMaker Helper. We want our users to feel that the tool is tailored for them, adapting to their specific needs and preferences, making video production a breeze.

## Powered by Python: Project Dependencies

VideoMaker Helper is a testament to the dynamic capabilities of the Python ecosystem. Crafted with passion in Brazil, this CLI stands tall on the shoulders of some exceptional Python projects. Here are the primary libraries and frameworks that make VideoMaker Helper tick:

- **[pydub](https://github.com/jiaaro/pydub)**: An intuitive library that simplifies audio processing, allowing us to manipulate and analyze sound effortlessly.

- **[moviepy](https://github.com/Zulko/moviepy)**: A versatile tool that empowers us to edit videos with a Pythonic touch, making complex video manipulations a breeze.

- **[Whisper](https://openai.com/research/publications/whisper-an-automatic-speech-recognition-system-for-conversational-speech/)**: OpenAI's automatic speech recognition (ASR) system. It's designed to convert spoken language into written text, making audio transcription efficient and accurate.

- **[pedalboard](https://github.com/spotify/pedalboard)**: Developed by Spotify, this library provides a robust platform for audio effects, further enhancing the audio capabilities of VideoMaker Helper.

These dependencies, among others, form the backbone of our tool, and we express our deepest gratitude to the developers and communities behind these projects. Their commitment to open-source innovation drives tools like VideoMaker Helper to push boundaries and redefine content creation.
