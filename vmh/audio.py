from itertools import chain
from pathlib import Path

from loguru import logger
from pydub import AudioSegment, silence
from tinydb import TinyDB, where

from .equalize import process_audio
from .settings import cache_db_path

db = TinyDB(str(cache_db_path))


def extract_audio(
    audio_file: str, output_file: str, eq: bool = True
) -> Path | tuple[Path, ...]:
    audio: AudioSegment = AudioSegment.from_file(audio_file)
    audio.export(output_file, format='wav')

    if eq:
        process_audio(output_file, 'eq_' + output_file)
        return Path(output_file), Path('eq_' + output_file)

    return Path(output_file)


def cut_silences(audio_file: str, output_file: str) -> Path:
    logger.info(f'Reading file: {audio_file}')
    audio = AudioSegment.from_file(audio_file)
    logger.info(f'File read: {audio_file}')

    silences = silence.split_on_silence(
        audio, min_silence_len=400, silence_thresh=-65
    )

    combined = AudioSegment.empty()
    for chunk in silences:
        combined += chunk

    combined.export(output_file, format='mp3')

    return Path(output_file)


def detect_silences(audio_file: str, *, force: bool = False):
    times = db.search(where('file_name') == audio_file)

    if not times or force:
        logger.info(f'Reading file: {audio_file}')
        audio = AudioSegment.from_file(audio_file)
        logger.info(f'File read: {audio_file}')

        logger.info(f'Analize silences in {audio_file}')
        silences = silence.detect_silence(
            audio, min_silence_len=400, silence_thresh=-65
        )
        logger.info(f'Finalized analysis: {audio_file}')

        times = list(
            chain.from_iterable(
                [(start / 1000) + 0.100, (stop / 1000) - 0.100]
                for start, stop in silences
            )
        )

        db.insert(
            {
                'file_name': str(audio_file),
                'times': times,
            }
        )

        return times

    else:
        logger.info('Using db cache!')
        return times[0]['times']
