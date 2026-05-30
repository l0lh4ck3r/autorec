import sqlite3


class Database:

    def __init__(self, db_path):

        self.conn = sqlite3.connect(db_path)

        self.conn.row_factory = sqlite3.Row

    def execute(self, query, params=()):

        cursor = self.conn.cursor()

        cursor.execute(query, params)

        self.conn.commit()

        return cursor

    def fetchall(self, query, params=()):

        cursor = self.conn.cursor()

        cursor.execute(query, params)

        return cursor.fetchall()

    def fetchone(self, query, params=()):

        cursor = self.conn.cursor()

        cursor.execute(query, params)

        return cursor.fetchone()