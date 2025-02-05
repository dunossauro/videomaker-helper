import pytest
from tinydb import TinyDB

from videomaker_helper.audio import detect_silences


@pytest.fixture
def cache_db(monkeypatch, tmp_path) -> TinyDB:
    from videomaker_helper import audio

    d = tmp_path / 'tests'
    d.mkdir()

    monkeypatch.setattr(audio, 'db', TinyDB(d / 'wip.json'))

    return audio.db


def test_check_cache_detect_silences_default(cache_db):
    input_file = 'tests/test_assets/sas.wav'
    detect_silences(input_file)
    db_record = cache_db.all()[0]

    assert db_record['silence_time'] == 400  # noqa: PLR2004 (default value)
    assert db_record['threshold'] == -65  # noqa: PLR2004 (default value)
    assert db_record['type'] == 'silence'


@pytest.mark.parametrize('threshold, silence_time', [(-10, 20), (-20, 50)])
def test_check_cache_detect_silences_variations(
    threshold, silence_time, cache_db
):
    input_file = 'tests/test_assets/sas.wav'

    detect_silences(input_file, threshold=threshold, silence_time=silence_time)

    db_record = cache_db.all()[0]

    assert db_record['silence_time'] == silence_time
    assert db_record['threshold'] == threshold
