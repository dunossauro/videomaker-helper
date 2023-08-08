from itertools import chain, islice, pairwise
from pathlib import Path

from loguru import logger
from parsel.selector import Selector
from pydub import AudioSegment, silence
from tinydb import TinyDB, where

db = TinyDB('cache.json')

xml_template = """ <entry producer="{}" in="00:00:{:.3f}" out="00:00:{:.3f}">
   <property name="kdenlive:id">{}</property>
  </entry>
"""


def read_silences(audio_file: str):
    times = db.search(where('file_name') == audio_file)

    if not times:
        logger.info(f'Reading file: {audio_file}')
        audio = AudioSegment.from_file(audio_file)
        logger.info(f'File read: {audio_file}')

        logger.info(f'Analize silences in {audio_file}')
        silences = silence.detect_silence(
            audio, min_silence_len=400, silence_thresh=-65
        )
        logger.info(f'Finalized analysis: {audio_file}')

        times = chain.from_iterable(
            [(start / 1000) + 0.100, (stop / 1000) - 0.100]
            for start, stop in silences
        )

        db.insert(
            {
                'file_name': str(audio_file),
                'times': list(times),
            }
        )
    else:
        logger.info('Using db cache!')
        times = times[0]['times']

    return times


def check_chain(video_file: Path, input_file: Path) -> tuple[str | None, ...]:
    with open(input_file) as f:
        content = f.read()
        s = Selector(content)
        el = s.xpath(f'//chain/property[text() = "{video_file.name}"]/..')

        _chain = el.css('chain::attr("id")').get()
        _id = el.css('property[name="kdenlive:id"]::text').get()

        playlist_id = (
            s.xpath(f'//playlist/entry[@producer="{_chain}"]/..')
            .xpath('@id')
            .get()
        )

        return _chain, _id, playlist_id


def write_file(silences, filename, chain, _id):
    logger.info('Start file', filename)

    with open(filename, 'w') as f:
        for start, stop in islice(pairwise(silences), 1, None, 2):
            if start < 0:
                start = 0.0
            f.write(xml_template.format(chain, start, stop, _id))

    logger.info('End file', filename)


def cut(audio_file, video_file, input_file, output_path: Path):
    times = read_silences(str(audio_file))

    logger.info('Start video chain')
    chain_id, file_id, _ = check_chain(video_file, input_file)
    write_file(times, output_path / 'video.xml', chain_id, file_id)

    logger.info('Start audio chain')
    chain_id, file_id, _ = check_chain(audio_file, input_file)
    write_file(times, output_path / 'audio.xml', chain_id, file_id)
