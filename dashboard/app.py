from flask import Flask
from flask import render_template

import sqlite3

app = Flask(__name__)


@app.route("/")
def index():

    db = sqlite3.connect(
        "latest.db"
    )

    assets = db.execute(
        """
        SELECT *
        FROM asset_inventory
        """
    ).fetchall()

    findings = db.execute(
        """
        SELECT *
        FROM findings
        ORDER BY score DESC
        """
    ).fetchall()

    return render_template(
        "dashboard.html",
        assets=assets,
        findings=findings
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )