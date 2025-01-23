from pathlib import Path

from platformdirs import user_data_dir

user_path = Path(user_data_dir('vmh', 'vmh', ensure_exists=True))
cache_db_path = user_path / 'vmh_cache.json'
eq_config_path = user_path / 'config.json'

# Create base config files
if not cache_db_path.exists():
    cache_db_path.touch()

if not eq_config_path.exists():
    eq_config_path.touch()

__version__ = '0.1.0'
