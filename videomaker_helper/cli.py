import warnings
from pathlib import Path
from typing import Annotated

from cyclopts import App, Parameter
from loguru import logger
from rich.console import Console

from videomaker_helper import audio, cache, plot, video
from videomaker_helper.equalize import process_audio
from videomaker_helper.kdenlive import cut
from videomaker_helper.settings import __version__

warnings.filterwarnings('ignore')

path_arg = Annotated[Path, Parameter(help='Path to the file')]
console = Console()

app = App(
    version=__version__,
    help='Videomaker Helper!',
    version_flags=['--version', '-v'],
)
app.command(cache.cache, name='cache')
app.command(plot.plot, name='plot')


# Options
silence_option = Annotated[
    int,
    Parameter(
        name=['--silence-time', '-s'],
        help='Minimal time in ms for configure a silence',
    ),
]

threshold_option = Annotated[
    int,
    Parameter(
        name=['--threshold', '-t'],
        help='Value in db for detect silence',
    ),
]

distance_option = Annotated[
    audio.Distance,
    Parameter(
        name=['--distance', '-d'],
        help='Distance between silences',
    ),
]

force_option = Annotated[bool, Parameter(help='Ignore cache')]


@app.command()
def extract_audio(
    video_file: path_arg,
    output_file: Path = Path('output.wav'),
    /,
    *,
    eq: Annotated[
        bool,
        Parameter(
            help='Add compression and 10db of extracted audio',
        ),
    ] = False,
):
    """Extracts the audio from a video."""
    console.print(audio.extract_audio(str(video_file), str(output_file), eq))


@app.command()
def cut_silences(
    audio_file: path_arg,
    output_file: path_arg,
    /,
    *,
    silence_time: silence_option = 400,
    threshold: threshold_option = -65,
    distance: distance_option = audio.Distance.tiny,
):
    """Removes all silences from an audio file."""
    console.print(
        audio.cut_silences(
            str(audio_file),
            str(output_file),
            silence_time=silence_time,
            threshold=threshold,
        ),
    )


@app.command()
def equalize(
    audio_file: path_arg,
    output_file: Path = Path('output.wav'),
    /,
):
    """Add effects for audio file."""
    process_audio(str(audio_file.resolve()), str(output_file))

    console.print(f'{output_file} Created')


@app.command()
def kdenlive(
    input_xml: path_arg,
    video_file: path_arg,
    output_path: Path = Path('cuts.kdenlive'),
    audio_file: Annotated[
        Path,
        Parameter(
            help='Optional audio equilized audio file',
        ),
    ] = Path(),
    /,
    *,
    silence_time: Annotated[int, silence_option] = 400,
    threshold: Annotated[int, threshold_option] = -65,
    distance: distance_option = audio.Distance.tiny,
    force: force_option = False,
):
    """Generates an XML compatible with kdenlive settings.

    Note: It doesn’t directly modify kdenlive files.
    It new kdenlive file with [OUTPUT_FILE].
    """  # noqa: W505
    # TODO(dunossauro): Ask if input_xml and output_path are same!
    output_path = output_path.resolve()
    if output_path.exists():
        logger.info(f'Deleting {output_path}')
        output_path.unlink()

    console.print(
        cut(
            audio_file.resolve(),
            video_file.resolve(),
            input_xml.resolve(),
            output_path.resolve(),
            silence_time,
            threshold,
            force,
            distance.value,
        ),
    )


@app.command()
def cut_video(
    video_file: path_arg,
    output_path: Path = Path('result.mp4'),
    audio_file: Annotated[
        str,
        Parameter(
            help='Optional audio equilized audio file',
        ),
    ] = '',
    /,
    *,
    silence_time: silence_option = 400,
    threshold: threshold_option = -65,
    distance: distance_option = audio.Distance.tiny,
    codec: Annotated[
        video.Codec, Parameter(name=['--codec', '-c'])
    ] = video.Codec.mpeg4,
    preset: Annotated[
        video.Preset, Parameter(name=['--preset', '-p'])
    ] = video.Preset.medium,
    bitrare: Annotated[str, Parameter(name=['--bitrate', '-b'])] = '15M',
    force: force_option = False,
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


if __name__ == '__main__':
    app()
