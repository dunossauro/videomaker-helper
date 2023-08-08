from pathlib import Path
from subprocess import Popen
from shutil import rmtree
from typing import Annotated

from loguru import logger
from rich.console import Console
from tinydb import TinyDB
from typer import Argument, Typer

from vmh.audio_cuts import cut, read_silences
from vmh.equalize import process_audio

path_arg = Annotated[Path, Argument()]

app = Typer()
console = Console()
db = TinyDB('cache.json')


@app.command()
def extract_audio(file):
    """Extrai o audio de um vídeo."""
    path = Path(file)
    result = Popen(
        f'ffmpeg -i {str(path)} -vn -acodec copy {path.stem}.wav -y'.split()
    )
    result.wait()


@app.command()
def silences(audio_file: path_arg):
    """Verifica os silencios em um arquivo.

    As verificações são armazenadas em cache
        caso o arquivo já tenha sido analisado, retornará o cache.
    """
    console.print(read_silences(str(audio_file)))


@app.command()
def list_cache():
    """Mostra o cache."""
    console.print(db.all())


@app.command()
def equalize(
    audio_file: path_arg,
    output_file: Path = Argument(default='output.wav'),
):
    """Adiciona compressão, 10db de ganho e um limiter de -10"""
    process_audio(str(audio_file.resolve()), str(output_file))

    console.print(f'{output_file} Created')


@app.command()
def kdenlive(
    audio_file: path_arg,
    video_file: path_arg,
    input_xml: path_arg,
    output_path: path_arg,
):
    """Gera um xml compatível com a configuração do kdenlive.

    Ele não aplica ao arquivo do kdenlive, somente gera o conteúdo da timeline,
        você deve adicionar manualmente.
    """
    if output_path.exists():
        logger.info(f'Deleting {output_path}')
        # output_path.rmdir()
        rmtree(output_path)

    output_path.mkdir()

    cut(audio_file, video_file, input_xml, output_path)
