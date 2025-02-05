# 📹 VideoMaker Helper

> This project is at a very early stage of development, bugs and lack of documentation are expected at this stage.

VideoMaker Helper is a collection of command-line utilities designed to simplify common tasks for video and audio content creators. These tools aim to automate specific aspects of the video-making process, reducing manual work and enhancing overall efficiency.

## 🥝 Core Features:

- **Silence Detection**: Automatically detect silent segments in audio files. Useful for determining parts to edit or skip.

- **Audio Equalization**: Adjust the audio to a consistent level across a file. This tool can add compression and gain to improve the listening experience.

- **Audio Extraction**: Pull audio content from video files. With an option to receive both the raw extracted audio and an equalized version.

- **Video Editing**: Based on silence detection, automatically cut portions of a video, providing a streamlined content experience. See the examples at [**video-cut examples**](https://github.com/dunossauro/videomaker-helper/tree/main/examples/cut-video)

## Installation:

To install VideoMaker Helper, simply use the following command:

```bash
pipx install git+https://github.com/dunossauro/videomaker-helper.git
```

With VideoMaker Helper installed, you can easily run any of the included tools from your terminal. It's a practical toolset for anyone looking to expedite their content creation process.


![type:video](videos/result_large.mp4){: disable-global-config style='width: 100%'}
