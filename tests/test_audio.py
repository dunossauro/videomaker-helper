from itertools import chain
from pathlib import Path
from typing import cast

from pydub import AudioSegment

from vmh.audio import (
    _audio_chain,
    cut_silences,
    detect_silences,
    extract_audio,
)

audio_stub = {
    'path': 'tests/test_assets/audio_test.wav',
    'silences': [
        [1610, 2257],
        [2548, 3237],
        [3570, 4454],
        [5018, 6057],
        [6815, 7901],
        [9256, 9811],
        [9812, 10249],
        [10901, 11655],
        [11717, 12432],
    ],
    'chain': [
        1.61,
        2.257,
        2.548,
        3.237,
        3.57,
        4.454,
        5.018,
        6.057,
        6.815,
        7.901,
        9.256,
        9.811,
        9.812,
        10.249,
        10.901,
        11.655,
        11.717,
        12.432,
    ],
}


def test__audio_chains():
    assert _audio_chain(audio_stub['silences'], 'tiny') == audio_stub['chain']


def test_detect_silences_tiny():
    silences = detect_silences(audio_stub['path'], distance='tiny', force=True)
    assert silences == audio_stub['chain']


def test_detect_silences_small():
    small_distance = 0.100

    silences = detect_silences(
        audio_stub['path'],
        distance='small',
        force=True,
    )

    times = chain.from_iterable(
        [
            (start / 1000) + small_distance,
            (stop / 1000) - small_distance,
        ]
        for start, stop in audio_stub['silences']
    )

    assert silences == list(times)


def test_detect_silences_negative():
    negative_distance = 0.100

    silences = detect_silences(
        audio_stub['path'],
        distance='small',
        force=True,
    )

    times = chain.from_iterable(
        [
            (start / 1000) + negative_distance,
            (stop / 1000) - negative_distance,
        ]
        for start, stop in audio_stub['silences']
    )

    assert silences == list(times)


def test_extract_audio_no_eq(tmpdir):
    output = tmpdir / 'out.mp3'
    expected_seconds = 2

    result = extract_audio(
        'tests/test_assets/colorbar.mp4',
        str(output),
        eq=False,
    )

    audio_seg = AudioSegment.from_wav(str(result))
    assert int(len(audio_seg) / 1000) == expected_seconds


def test_extract_audio_no_eq_name_output(tmpdir):
    output = tmpdir / 'out.mp3'

    result = extract_audio(
        'tests/test_assets/colorbar.mp4',
        str(output),
        eq=False,
    )

    result = cast(Path, result)
    assert result.name == 'out.mp3'


def test_extract_audio_with_eq_name_output(tmpdir):
    output = tmpdir / 'out.mp3'

    result_pure, result_eq = extract_audio(
        'tests/test_assets/colorbar.mp4',
        str(output),
        eq=True,
    )

    assert result_pure.name == 'out.mp3'
    assert result_eq.name == 'eq_out.mp3'


def test_extract_audio_with_eq(tmpdir):
    output = tmpdir / 'out.wav'
    expected_seconds = 2

    result_pure, result_eq = extract_audio(
        'tests/test_assets/colorbar.mp4',
        str(output),
        eq=True,
    )

    audio_seg = AudioSegment.from_wav(str(result_pure))
    assert int(len(audio_seg) / 1000) == expected_seconds

    audio_seg = AudioSegment.from_wav(str(result_eq))
    assert int(len(audio_seg) / 1000) == expected_seconds


def test_cut_audio_silences(tmpdir):
    inpurt_file = 'tests/test_assets/sas.wav'
    output_file = tmpdir / 'out.mp3'
    expected_size = 1
    cut_silences(inpurt_file, output_file)

    audio_seg: AudioSegment = AudioSegment.from_mp3(str(output_file))

    assert (len(audio_seg) / 1000) == expected_size
