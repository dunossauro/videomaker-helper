import warnings
from pathlib import Path
from shutil import rmtree
from typing import Annotated

from loguru import logger
from rich.console import Console
from typer import Argument, Context, Exit, Option, Typer

from vmh import audio, cache, video
from vmh.equalize import process_audio
from vmh.kdenlive import cut
from vmh.settings import __version__

warnings.filterwarnings('ignore')

path_arg = Annotated[Path, Argument()]
console = Console()

app = Typer(help='Videomaker Helper!', no_args_is_help=True)
app.add_typer(cache.cache, name='cache', help='Cache tools.')


# Options
silence_option = Option(
    400,
    '--silence-time',
    '-s',
    help='Minimal time in ms for configure a silence',
)

threshold_option = Option(
    -65, '--threshold', '-t', help='Value in db for detect silence'
)

distance_option = Option(
    audio.Distance.tiny,
    '--distance',
    '-d',
    help='Distance betweet silences',
)


def version(arg):
    if arg:
        print(__version__)
        raise Exit(code=0)


@app.callback(invoke_without_command=True)
def callcaback(
    ctx: Context,
    version: bool = Option(
        False,
        '--version',
        '-v',
        callback=version,
        is_eager=True,
        is_flag=True,
        case_sensitive=False,
        help='Show VMH version',
    ),
):
    ...


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
    audio_file: path_arg,
    silence_time: int = silence_option,
    threshold: int = threshold_option,
    distance: audio.Distance = distance_option,
    force: bool = Option(False, help='Ignore cache'),
):
    """Checks for silences in a audio file.

    The checks are cached, so if the file has already been analyzed, it will return the cache.
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
    silence_time: int = silence_option,
    threshold: int = threshold_option,
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
    gain: int = Option(10, '--gain', '-g', help='Add dbs in audio'),
):
    """Add Compression and Gain dor audio file."""
    process_audio(str(audio_file.resolve()), str(output_file), gain)

    console.print(f'{output_file} Created')


@app.command()
def kdenlive(
    audio_file: path_arg,
    video_file: path_arg,
    input_xml: path_arg,
    output_path: Path = Argument(default='timelines'),
    silence_time: int = silence_option,
    threshold: int = threshold_option,
    distance: audio.Distance = distance_option,
):
    """Generates an XML compatible with kdenlive settings.

    Note: It doesn’t directly modify kdenlive files. It creates timeline instructions which you must manually integrate.
    """
    if output_path.exists():
        logger.info(f'Deleting {output_path}')
        rmtree(output_path)

    output_path.mkdir()

    cut(
        audio_file,
        video_file,
        input_xml,
        output_path,
        silence_time,
        threshold,
        distance.value,
    )


@app.command()
def cut_video(
    video_file: path_arg,
    audio_file: str = Argument(
        default='', help='Optional audio equilized audio file'
    ),
    output_path: Path = Argument(default='result.mp4'),
    silence_time: int = silence_option,
    threshold: int = threshold_option,
    distance: audio.Distance = distance_option,
    codec: video.Codec = Option(video.Codec.mpeg4, '--codec', '-c'),
    preset: video.Preset = Option(video.Preset.medium, '--preset', '-p'),
    bitrare: str = Option('15M', '--bitrate', '-b'),
    force: bool = Option(default=False, help='Ignore cache'),
):
    """Edits a video using silences as reference."""
    video.cut_video(
        str(video_file),
        str(output_path),
        threshold=threshold,
        silence_time=silence_time,
        distance=distance.value,
        audio_file=audio_file,
        force=force,
        codec=codec,
        preset=preset,
        bitrate=bitrare,
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
