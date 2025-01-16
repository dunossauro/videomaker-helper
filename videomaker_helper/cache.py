from rich.console import Console
from tinydb import TinyDB
from typer import Abort, Typer, confirm

from videomaker_helper import settings

cache = Typer()
console = Console()
db = TinyDB(str(settings.cache_db_path))


@cache.command()
def list():
    """Displays cache."""
    console.print(db.all())


@cache.command()
def clear():
    """Clear cache."""
    delete = confirm('Are you sure you want to delete it cache?')
    if not delete:
        raise Abort()

    db.truncate()
