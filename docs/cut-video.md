# Cut Video

The `cut-video` command creates a new video by removing the silences present in the video file.

For example:

```
vmh cut-video sample.mp4
```

This will remove the silences and generate a file called `result.mp4`.

> You can find some examples of cuts [here](https://github.com/dunossauro/videomaker-helper/tree/main/examples/cut-video).

## Usage examples

### Simple cuts

To edit a video named `sample.mp4` using the default parameters, use:

```bash
vmh cut-video sample.mp4
```

This will remove the silences and generate a file called `result.mp4`.

### Cuts based on another audio file

Sometimes, we have a video file and an external audio file that is already equalized and processed.

We can cut the video based on the silences from this audio and generate a new file that removes the original audio from the video and replaces it with the new audio file:

```bash
vmh cut-video video_sample.mp4 --audio_file equalized_audio.wav
```

This way, the new video will have the equalized audio with the cuts already applied.

## Concepts and features

Silences are defined by the audio threshold and the minimum duration of silence found in the audio. As this is common for all cutting commands, the explanation can be found [here](threshold_and_distances.md).

## `--help` Flag Output:

```console exec="1" source="console" result="ansi"
$ vmh cut-video --help
```

## API for developers

::: videomaker_helper.video.cut_video
