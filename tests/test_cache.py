import pytest
from videomaker_helper.audio import detect_silences
from videomaker_helper.cache import db

from tinydb import where


def test_check_cache_detect_silences_default():
    input_file = 'tests/test_assets/sas.wav'
    detect_silences(input_file)
    db_record = db.search(where('file_name') == input_file)[0]

    assert db_record['silence_time'] == 400
    assert db_record['threshold'] == -65
    assert db_record['type'] == 'silence'


@pytest.mark.parametrize(
    'threshold, silence_time',
    [(-10, 20), (-20, 50)]
)
def test_check_cache_detect_silences_variations(threshold, silence_time):
    input_file = 'tests/test_assets/sas.wav'

    detect_silences(
        input_file, threshold=threshold, silence_time=silence_time
    )

    db_record = db.search(
        (where('file_name') == input_file)
        & (where('threshold') == threshold)
        & (where('silence_time') == silence_time)
    )[0]

    assert db_record['silence_time'] == silence_time
    assert db_record['threshold'] == threshold
