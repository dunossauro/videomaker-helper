from typer.testing import CliRunner

from vmh.cli import app
from vmh.settings import __version__

cli = CliRunner()


def test_cli_version():
    response = cli.invoke(app, '--version')

    assert __version__ in response.stdout
