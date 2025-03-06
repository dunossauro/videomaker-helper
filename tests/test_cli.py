from videomaker_helper.cli import app
from videomaker_helper.settings import __version__


def test_cli_version(capsys):
    app('--version')

    assert __version__ in capsys.readouterr().out
