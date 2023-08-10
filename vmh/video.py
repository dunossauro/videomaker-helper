from itertools import islice, pairwise

from loguru import logger
from moviepy.editor import AudioFileClip, VideoFileClip, concatenate_videoclips

from .audio import detect_silences


def cut_video(input_file: str, output_file: str, audio_file: str = ''):
    logger.info(f'Detecting silences on {input_file}')
    if audio_file:
        silences = detect_silences(audio_file, force=False)
        video = VideoFileClip(input_file)
        paudio = AudioFileClip(str(audio_file))
        video.audio = paudio
    else:
        silences = detect_silences(input_file)
        video = VideoFileClip(input_file)

    logger.info(f'Creating subclips on {input_file}')
    clips = [
        video.subclip(start, stop)
        for start, stop in islice(pairwise(silences), 1, None, 2)
    ]

    final_video = concatenate_videoclips(clips)

    logger.info(f'Writing {output_file}')
    final_video.write_videofile(
        output_file, codec='mpeg4'
    )  # , codec='rawvideo')
