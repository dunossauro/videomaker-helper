from enum import Enum
from itertools import chain
from pathlib import Path
from typing import Literal, TypedDict

from loguru import logger
from pydub import AudioSegment, silence
from tinydb import TinyDB, where

from .equalize import process_audio
from .settings import cache_db_path

db = TinyDB(str(cache_db_path))


class TranscribeModes(str, Enum):
    print = 'print'
    txt = 'txt'
    json = 'json'
    srt = 'srt'


class Distance(str, Enum):
    tiny = 'tiny'
    small = 'small'
    medium = 'medium'
    large = 'large'
    huge = 'huge'


threshold_distance: dict[str, float] = {
    'tiny': 0,
    'small': 0.100,
    'medium': 0.250,
    'large': 0.500,
    'huge': 1,
}


class Seguiment(TypedDict):
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: list[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float


def transcribe_audio(audio_path: Path, mode: str, output_path: str):
    from whisper import load_model  # Lazy load 2secs to start
    from whisper.utils import get_writer  # Lazy load

    cache = db.search(
        (where('file_name') == str(audio_path))
        & (where('type') == 'transcribe')
    )

    if not cache:
        model = load_model('base')
        result = model.transcribe(str(audio_path))
        db.insert(
            {
                'type': 'transcribe',
                'file_name': str(audio_path),
                'data': result,
            }
        )
    else:
        result = cache[0]['data']

    match mode:
        # TODO: Eliminar essas repetições
        case TranscribeModes.print:
            return result

        case TranscribeModes.json:
            writter = get_writer('json', '.')
            writter(
                result,
                output_path,
                {
                    'max_line_width': 50,
                    'max_line_count': 1,
                    'highlight_words': False,
                },
            )

        case TranscribeModes.srt:
            writter = get_writer('srt', '.')
            writter(
                result,
                output_path,
                {
                    'max_line_width': 50,
                    'max_line_count': 1,
                    'highlight_words': False,
                },
            )

        case TranscribeModes.txt:
            writter = get_writer('txt', '.')
            writter(
                result,
                output_path,
                {
                    'max_line_width': 50,
                    'max_line_count': 1,
                    'highlight_words': False,
                },
            )

    return output_path


def extract_audio(
    audio_file: str, output_file: str, eq: bool = True
) -> Path | tuple[Path, ...]:
    audio: AudioSegment = AudioSegment.from_file(audio_file)
    audio.export(output_file, format='wav')

    if eq:
        process_audio(output_file, 'eq_' + output_file)
        return Path(output_file), Path('eq_' + output_file)

    return Path(output_file)


def cut_silences(
    audio_file: str,
    output_file: str,
    silence_time: int = 400,
    threshold: int = -65,
) -> Path:
    logger.info(f'Reading file: {audio_file}')
    audio = AudioSegment.from_file(audio_file)
    logger.info(f'File read: {audio_file}')

    silences = silence.split_on_silence(
        audio, min_silence_len=silence_time, silence_thresh=threshold
    )

    combined = AudioSegment.empty()
    for chunk in silences:
        combined += chunk

    combined.export(output_file, format='mp3')

    return Path(output_file)


def detect_silences(
    audio_file: str,
    silence_time: int = 400,
    threshold: int = -65,
    distance: Literal['short', 'mid', 'long', 'sec'] = 'short',
    *,
    force: bool = False,
) -> list[float]:
    times = db.search(
        (where('file_name') == audio_file) & (where('type') == 'silence')
    )

    if not times or force:
        logger.info(f'Reading file: {audio_file}')
        audio = AudioSegment.from_file(audio_file)
        logger.info(f'File read: {audio_file}')

        logger.info(f'Analize silences in {audio_file}')
        silences = silence.detect_silence(
            audio, min_silence_len=silence_time, silence_thresh=threshold
        )
        logger.info(f'Finalized analysis: {audio_file}')

        times = list(
            chain.from_iterable(
                [
                    (start / 1000) + threshold_distance[distance],
                    (stop / 1000) - threshold_distance[distance],
                ]
                for start, stop in silences
            )
        )
        logger.debug(f'first 20 cuts {times[:20]}')

        db.insert(
            {
                'type': 'silence',
                'file_name': str(audio_file),
                'times': times,
            }
        )

        logger.info(f'Found {len(times)} silences in audio')
        return times

    else:
        logger.info('Using db cache!')
        return times[0]['times']
