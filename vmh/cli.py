import warnings
from pathlib import Path
from shutil import rmtree
from typing import Annotated

from loguru import logger
from rich.console import Console
from typer import Argument, Option, Typer

from vmh import audio, cache, video
from vmh.equalize import process_audio
from vmh.kdenlive import cut

warnings.filterwarnings('ignore')

path_arg = Annotated[Path, Argument()]
console = Console()

app = Typer(help='Videomaker Helper!')
app.add_typer(cache.cache, name='cache', help='Cache tools.')


@app.command()
def extract_audio(
    audio_file: path_arg,
    output_file: Path = Argument(default='output.wav'),
    eq: bool = Option(
        True, help='Add compression and 10db of extracted audio'
    ),
):
    """Extracts the audio from a video."""
    console.print(audio.extract_audio(str(audio_file), str(output_file), eq))


@app.command()
def silences(
    audio_file: list[path_arg],
    silence_time: int = Option(
        400, help='Minimal time in ms for configure a silence'
    ),
    threshold: int = Option(-65, help='Value in db for detect silence'),
    distance: audio.Distance = Option(audio.Distance.short),
    force: bool = Option(False, help='Ignore cache'),
):
    """Checks for silences in a audio file.

    As verificações são armazenadas em cache
        caso o arquivo já tenha sido analisado, retornará o cache.
    """
    console.print(
        list(
            audio.detect_silences(
                str(audio_file),
                silence_time=silence_time,
                threshold=threshold,
                distance=distance.value,
                force=force,
            )
        )
    )


@app.command()
def cut_silences(
    audio_file: path_arg,
    output_file: path_arg,
    silence_time: int = Option(
        400, help='Minimal time in ms for configure a silence'
    ),
    threshold: int = Option(-65, help='Value in db for detect silence'),
):
    """Removes all silences from an audio file."""
    console.print(
        audio.cut_silences(
            str(audio_file),
            str(output_file),
            silence_time=silence_time,
            threshold=threshold,
        )
    )


@app.command()
def equalize(
    audio_file: path_arg,
    output_file: Path = Argument(default='output.wav'),
):
    """Adds compression and 10db gain."""
    process_audio(str(audio_file.resolve()), str(output_file))

    console.print(f'{output_file} Created')


@app.command()
def kdenlive(
    audio_file: path_arg,
    video_file: path_arg,
    input_xml: path_arg,
    output_path: Path = Argument(default='timelines'),
):
    """Generates an XML compatible with kdenlive settings.

    Ele não aplica ao arquivo do kdenlive, somente gera o conteúdo da timeline,
        você deve adicionar manualmente.
    """
    if output_path.exists():
        logger.info(f'Deleting {output_path}')
        rmtree(output_path)

    output_path.mkdir()

    cut(audio_file, video_file, input_xml, output_path)


@app.command()
def cut_video(
    video_file: path_arg,
    audio_file: str = Argument(default=''),
    output_path: Path = Argument(default='result.mp4'),
    silence_time: int = Option(
        400, help='Minimal time in ms for configure a silence'
    ),
    threshold: int = Option(-65, help='Value in db for detect silence'),
    distance: audio.Distance = Option(audio.Distance.short),
    codec: video.Codec = Option(video.Codec.mpeg4),
):
    """Edits a video using silences as reference."""
    video.cut_video(
        str(video_file),
        str(output_path),
        threshold=threshold,
        silence_time=silence_time,
        distance=distance.value,
        audio_file=audio_file,
        codec=codec.value,
    )


@app.command()
def transcribe(
    audio_path: Path = Argument(),
    mode: audio.TranscribeModes = audio.TranscribeModes.srt,
    output_path: str = Argument(default='output.srt'),
):
    """Transcribes an audio file into subtitles."""
    console.print(audio.transcribe_audio(audio_path, mode, output_path))


@app.command()
def grammar_check(file: path_arg, lang: str = Argument(default='pt-BR')):
    """Check grammar in a tex tfile."""
    from language_tool_python import LanguageTool  # lazy load

    tool = LanguageTool(lang)

    with open(file) as f:
        console.print(tool.check(f.read()))


if __name__ == '__main__':
    app()
