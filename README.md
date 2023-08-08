# VideoMaker Helper

This repository is just, at least for now, to sketch ideas about some tools I want to develop to make my life easier.

## DreamTools

Some tools I would like to develop.

### AudioSplitter - TODO
Separate multiple stereo audio channels from a single video file.

For example: A 7.1 video to 7 stereo files.

#### Possible solution

Use ffmpeg: https://trac.ffmpeg.org/wiki/AudioChannelManipulation

### VoiceCleaner - TODO

Clean audiofile with voice. Removing mouth clicks, essers, breath.

#### Possible solution

Use [pedalboard](https://github.com/spotify/pedalboard) to load VST plugins.

### AudioSlicer - TODO

Detect silences in audio and export this in OpentimelineIO file.

#### Possible solution

1. For detect silences in audio, we can use [pydub](https://github.com/jiaaro/pydub)
2. For timelines, we can use [OpenTimelineIO](https://opentimelineio.readthedocs.io/en/latest/index.html#)
3. Kdenlive is compatible with OpenTimelineIO. REF: https://kdenlive.org/en/2020/04/kdenlive-20-04-is-out/

### TimelineSlicer - WIP

Use audio with silence to create cuts in vídeos on kdenlive timeline.

#### Possible solution

Apply the same cuts with audio silences in vídeo.
