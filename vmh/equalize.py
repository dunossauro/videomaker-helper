from pedalboard import Compressor, Gain, Pedalboard
from pedalboard.io import AudioFile

board = Pedalboard([Compressor(), Gain(5)])


def process_audio(input_file, output_file='output.wav'):
    with AudioFile(input_file, 'r') as f:
        with AudioFile(output_file, 'w', f.samplerate, f.num_channels) as o:

            while f.tell() < f.frames:
                chunk = f.read(int(f.samplerate))
                effected = board(chunk, f.samplerate, reset=False)
                o.write(effected)
