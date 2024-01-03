from enum import Enum
from itertools import islice, pairwise
from typing import Literal

from loguru import logger
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips

from vmh.audio import detect_silences


class Preset(str, Enum):
    """FFMPeg presets.

    Font: https://trac.ffmpeg.org/wiki/Encode/H.264#Preset
    """

    ultrafast = 'ultrafast'
    superfast = 'superfast'
    veryfast = 'veryfast'
    faster = 'faster'
    fast = 'fast'
    medium = 'medium'
    slow = 'slow'
    slower = 'slower'
    veryslow = 'veryslow'


class Codec(str, Enum):
    """moviepy.readthedocs.io/en/latest/ref/videotools.html#moviepy.video.tools.credits.CreditsClip.write_videofile."""

    libx264 = 'libx264'
    mpeg4 = 'mpeg4'
    rawvideo = 'rawvideo'
    png = 'png'
    libvorbis = 'libvorbis'
    libvpx = 'libvpx'


def cut_video(
    input_file: str,
    output_file: str,
    silence_time: int,
    threshold: int,
    distance: Literal[
        'negative', 'tiny', 'small', 'medium', 'large', 'huge',
    ] = 'tiny',
    bitrate: str = '15M',
    codec: Codec = Codec.mpeg4,
    audio_file: str = '',
    preset: Preset = Preset.medium,
    force: bool = True,
):
    logger.info(f'Detecting silences on {input_file}')
    if audio_file:
        silences = detect_silences(
            audio_file,
            force=force,
            threshold=threshold,
            silence_time=silence_time,
            distance=distance,
        )
        video = VideoFileClip(input_file)
        paudio = AudioFileClip(str(audio_file))
        video.audio = paudio
    else:
        silences = detect_silences(
            input_file,
            force=force,
            threshold=threshold,
            silence_time=silence_time,
            distance=distance,
        )
        video = VideoFileClip(input_file)

    logger.info(f'Creating subclips on {input_file}')
    clips = [
        video.subclip(start, stop)
        for start, stop in islice(pairwise(silences), 1, None, 2)
    ]

    final_video = concatenate_videoclips(clips)

    logger.info(f'Writing {output_file}')
    final_video.write_videofile(
        output_file,
        codec=codec.value,
        preset=preset.value,
        bitrate=bitrate,
    )
