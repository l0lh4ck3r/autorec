from pathlib import Path

from database.db import Database


def initialize_database(db_path):

    db = Database(db_path)

    schema_file = (
        Path(__file__)
        .parent
        / "schema.sql"
    )

    schema = schema_file.read_text()

    db.conn.executescript(schema)

    db.conn.commit()

    return db