import sqlite3
from flask import current_app, g

from server.logger import logger

db_logger = logger.Logger('DB', 'blue')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            'app.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

        return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = sqlite3.connect(
            'app.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    with current_app.open_resource('schema.sql') as f:
        db_logger.log('Setting up database for further use')
        db.executescript(f.read().decode('utf8'))

def init_app(app):
    app.teardown_appcontext(close_db)
    init_db()
