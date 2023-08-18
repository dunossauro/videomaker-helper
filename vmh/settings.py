from pathlib import Path

from appdirs import user_data_dir

user_path = Path(user_data_dir('vmh', 'vmh'))
cache_db_path = user_path / 'vmh_cache.json'

__version__ = '0.1.0'
