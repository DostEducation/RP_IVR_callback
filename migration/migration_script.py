from api import db, app, models
import click
from flask.cli import with_appcontext


@click.command(name="migrate")
@with_appcontext
def migrate():
    db.create_all()


app.cli.add_command(migrate)
