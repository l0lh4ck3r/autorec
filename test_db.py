from pathlib import Path

import sqlite3

db_file = max(
    Path("output")
    .glob("*/scan.db")
)

conn = sqlite3.connect(
    db_file
)

print(
    conn.execute(
        "SELECT * FROM scans"
    ).fetchall()
)

print(
    conn.execute(
        "SELECT * FROM findings"
    ).fetchall()
)