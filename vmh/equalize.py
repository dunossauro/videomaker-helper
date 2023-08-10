from pathlib import Path

from pedalboard import Compressor, Gain, Pedalboard
from pedalboard.io import AudioFile

board = Pedalboard([Compressor(), Gain(7)])


def process_audio(input_file: str, output_file='output.wav') -> Path:
    with AudioFile(input_file, mode='r') as f:
        with AudioFile(output_file, 'w', f.samplerate, f.num_channels) as o:
            while f.tell() < f.frames:
                chunk = f.read(int(f.samplerate))
                effected = board(chunk, f.samplerate, reset=False)
                o.write(effected)

    return Path(output_file)
