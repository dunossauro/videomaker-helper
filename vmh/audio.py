from enum import Enum
from itertools import chain
from pathlib import Path
from typing import Literal, TypedDict

from loguru import logger
from pydub import AudioSegment, silence
from tinydb import TinyDB, where

from vmh.equalize import process_audio
from vmh.settings import cache_db_path

db = TinyDB(str(cache_db_path))


class TranscribeModes(str, Enum):
    print = 'print'
    txt = 'txt'
    json = 'json'
    srt = 'srt'


class Distance(str, Enum):
    negative = 'negative'
    tiny = 'tiny'
    small = 'small'
    medium = 'medium'
    large = 'large'
    huge = 'huge'


threshold_distance: dict[str, float] = {
    'negative': -0.100,
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


def transcribe_audio(
    audio_path: Path,
    mode: Literal['print', 'json', 'txt', 'srt'],
    output_path: str,
):
    from whisper import load_model  # Lazy load 2secs to start
    from whisper.utils import get_writer  # Lazy load

    cache = db.search(
        (where('file_name') == str(audio_path))
        & (where('type') == 'transcribe'),
    )

    if not cache:
        model = load_model('base')
        result = model.transcribe(str(audio_path))
        db.insert(
            {
                'type': 'transcribe',
                'file_name': str(audio_path),
                'data': result,
            },
        )
    else:
        result = cache[0]['data']

    match mode:
        # TODO: Eliminar essas repetições
        case 'print':
            return result

        case 'json':
            writer = get_writer('json', '.')
            writer(
                result,
                output_path,
                {
                    'max_line_width': 50,
                    'max_line_count': 1,
                    'highlight_words': False,
                },
            )

        case 'srt':
            writer = get_writer('srt', '.')
            writer(
                result,
                output_path,
                {
                    'max_line_width': 50,
                    'max_line_count': 1,
                    'highlight_words': False,
                },
            )

        case 'txt':
            writer = get_writer('txt', '.')
            writer(
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
    video_file: str, output_file: str, eq: bool = True,
) -> Path | tuple[Path, ...]:
    """Extract audio from vídeo.

    Args:
        video_file: Video to extract audio
        output_file:
        eq:

    Returns:
        A audio Path
    """
    audio: AudioSegment = AudioSegment.from_file(video_file)
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
        audio, min_silence_len=silence_time, silence_thresh=threshold,
    )

    combined = AudioSegment.empty()
    for chunk in silences:
        combined += chunk

    combined.export(output_file, format='mp3')

    return Path(output_file)


def _audio_chain(silences, distance):
    return list(
        chain.from_iterable(
            [
                (start / 1_000) + threshold_distance[distance],
                (stop / 1_000) - threshold_distance[distance],
            ]
            for start, stop in silences
        ),
    )


def detect_silences(
    audio_file: str,
    silence_time: int = 400,
    threshold: int = -65,
    distance: Literal[
        'negative', 'tiny', 'small', 'medium', 'large', 'huge',
    ] = 'tiny',
    *,
    force: bool = False,
) -> list[float]:
    times = db.search(
        (where('file_name') == audio_file)
        & (where('type') == 'silence')
        & (where('distance') == distance),
    )

    if not times or force:
        logger.info(f'Reading file: {audio_file}')
        audio = AudioSegment.from_file(audio_file)
        logger.info(f'File read: {audio_file}')

        logger.info(f'Analyze silences in {audio_file}')
        silences = silence.detect_silence(
            audio, min_silence_len=silence_time, silence_thresh=threshold,
        )

        logger.info(f'Finalized analysis: {audio_file}')

        times = _audio_chain(silences, distance)
        logger.debug(f'first 20 cuts {times[:20]}')

        db.insert(
            {
                'type': 'silence',
                'file_name': str(audio_file),
                'times': times,
                'distance': distance,
            },
        )

        logger.info(f'Found {len(times)} silences in audio')
        return times

    else:
        logger.info('Using db cache!')
        return times[0]['times']
