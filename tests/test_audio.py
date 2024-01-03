from itertools import chain

import pytest

from vmh.audio import _audio_chain, detect_silences, transcribe_audio

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
        audio_stub['path'], distance='small', force=True,
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
        audio_stub['path'], distance='small', force=True,
    )

    times = chain.from_iterable(
        [
            (start / 1000) + negative_distance,
            (stop / 1000) - negative_distance,
        ]
        for start, stop in audio_stub['silences']
    )

    assert silences == list(times)


@pytest.mark.skip(reason='Need cuda to run this on CI')
def test_transcribe_audio():
    segments = transcribe_audio(audio_stub['path'], 'print', '')['segments']
    for segment in segments:
        assert 'Isso é um teste.' in segment['text']
