# VideoMaker Helper

Micro tools to help content creators!


## Install

`pipx install https://github.com/dunossauro/videomaker-helper.git`


## Tools

### extract-audio

Extracts the audio from a video file.

Usage:

`vmh extract-audio <audio_path>`

### silences

TODO doc

### cut-silences

TODO doc

### equilize

TODO doc

### kdenlive

TODO doc

### cut-video

Create a new video with silences cuted

Only video:
`vmh cut-video <video_file> <output_path>`

Vídeo with external audio:
`vmh cut-video <video_file> <audio_path> <output_path>`

### transcribe

Transcribes an audio file into subtitles.

Usage:
`vmh transcribe <audio_path>`


### Usage

```bash
vmh --help

Usage: vmh [OPTIONS] COMMAND [ARGS]...

╭─ Commands ───────────────────────────────────────────────────────────────────────╮
│ cut-silences             Corta todos os silêncios de um arquivo de áudio         │
│ cut-video                Corta um vídeo usando os silêncios como base.           │
│ equalize                 Adiciona compressão, 10db de ganho                      │
│ extract-audio            Extrai o audio de um vídeo.                             │
│ kdenlive                 Gera um xml compatível com a configuração do kdenlive.  │
│ list-cache               Mostra o cache.                                         │
│ silences                 Verifica os silencios em um arquivo.                    │
│ transcribe               Transcribes an audio file into subtitles.               │
╰──────────────────────────────────────────────────────────────────────────────────╯
```
