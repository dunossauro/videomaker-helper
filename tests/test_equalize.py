from pedalboard import Gain, Pedalboard
from pydub import AudioSegment

from videomaker_helper.equalize import process_audio


def test_process_audio_dummy_pedalboard(tmpdir):
    input_file = 'tests/test_assets/audio_test.wav'
    out_file = str(tmpdir / 'out.wav')
    result_file = process_audio(
        input_file,
        out_file,
        board=Pedalboard(plugins=[Gain(5)]),
    )

    a = AudioSegment.from_wav(input_file)
    b = AudioSegment.from_wav(str(result_file))
    assert len(a) == len(b)


def test_process_audio_gain_pedalboard(tmpdir):
    input_file = 'tests/test_assets/audio_test.wav'
    out_file = str(tmpdir / 'out.wav')
    result_file = process_audio(
        input_file,
        out_file,
        board=Pedalboard(plugins=[Gain(5)]),
    )

    a: AudioSegment = AudioSegment.from_wav(input_file)
    b: AudioSegment = AudioSegment.from_wav(str(result_file))
    assert a.max < b.max
