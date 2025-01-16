from typer.testing import CliRunner

from videomaker_helper.cli import app
from videomaker_helper.settings import __version__

cli = CliRunner()


def test_cli_version():
    response = cli.invoke(app, '--version')

    assert __version__ in response.stdout
