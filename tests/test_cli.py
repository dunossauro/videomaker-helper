import pytest
from typer.testing import CliRunner

from vmh.cli import app
from vmh.settings import __version__

cli = CliRunner()


def test_cli_version():
    response = cli.invoke(app, '--version')

    assert __version__ in response.stdout


@pytest.mark.slow('LanguageTool take seconds to start!')
def test_grammar_check():
    response = cli.invoke(
        app, 'grammar-check tests/test_assets/grammar_file.txt'
    )

    assert 'UPPERCASE_SENTENCE_START' in response.stdout
