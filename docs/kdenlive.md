# kdenlive

The `kdenlive` command facilitates video editors by generating XML files compatible with kdenlive settings, focusing specifically on automating the process of cutting silences from video timelines. This utility is especially designed to expedite the editing workflow, allowing users to jumpstart their projects with silences already trimmed, effectively eliminating one of the most time-consuming and tedious aspects of video editing.

> ⚠️ Instability Alert: The interface for the kdenlive command is currently unstable. Users should anticipate potential modifications in future updates.

#### Main Features:

- **Automatic Silence-Cut Generation**: VMH harnesses the `silences` command's capabilities to detect silent portions in your audio file. These detected silences are then converted into kdenlive-compatible XML cut instructions, effectively pre-empting the need for manual audio silence trimming.

- **Efficient XML Creation for Kdenlive**: This command abstracts away the complexities of kdenlive's XML structure. Instead of fumbling with XML details, users can generate the required XML content for their timelines swiftly and effortlessly.

- **Fine-Tuned Silence Detection**: Video editors can customize the silence detection parameters to suit their specific requirements:
  - `--silence-time`: Sets the minimum duration for a segment to be recognized as silence.
  - `--threshold`: Determines the decibel level to qualify a segment as silent.
  - `--distance`: Adjusts the granularity of silence detection, with options from short intervals to exact durations.

#### Sample Commands:

1. For an automated silence-trimmed XML setup using `audio.wav`, `video.mp4`, and `project.xml`:
```bash
vmh kdenlive project.kdenlive video.mp4
```

2. Customizing silence detection parameters for the XML generation:
```bash
vmh kdenlive project.kdenlive video.mp4 --silence-time 500 --threshold -30
```

3. Using equilized audio
```bash
vmh kdenlive project.kdenlive video.mp4 audio.mp3
```


#### `--help` Option Display:

A snapshot of available options and arguments for the `kdenlive` command:


```console exec="1" source="console" result="ansi"
$ vmh kdenlive --help
```

## API for developers

::: videomaker_helper.kdenlive.cut
