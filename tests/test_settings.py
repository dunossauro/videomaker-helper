from videomaker_helper.settings import cache_db_path, eq_config_path, user_path


def test_check_user_path():
    assert user_path.name == 'vmh'


def test_check_cache_db_path():
    assert cache_db_path.parents[0].name == 'vmh'
    assert cache_db_path.name == 'vmh_cache.json'


def test_check_eq_config_path():
    assert eq_config_path.parents[0].name == 'vmh'
    assert eq_config_path.name == 'config.json'
