from flask import (
    Flask,
    render_template,
    send_file,
    request
)

from pathlib import Path

import sqlite3

app = Flask(__name__)

DB_FILE = "latest.db"


def query_one(sql):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(sql)

    value = cur.fetchone()[0]

    conn.close()

    return value

def query_all(sql):

    conn = sqlite3.connect(DB_FILE)

    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute(sql)

    rows = cur.fetchall()

    conn.close()

    return rows


@app.route("/")
def index():

    stats = {
        "assets":
            query_one(
                "SELECT COUNT(*) FROM asset_inventory"
            ),

        "urls":
            query_one(
                "SELECT COUNT(*) FROM url_inventory"
            ),

        "findings":
            query_one(
                "SELECT COUNT(*) FROM findings"
            ),

        "technologies":
            query_one(
                "SELECT COUNT(*) FROM technologies"
            ),

        "screenshots":
            query_one(
                "SELECT COUNT(*) FROM screenshots"
            ),
    }

    return render_template(
        "index.html",
        stats=stats
    )

@app.route("/assets")
def assets():

    assets = query_all(
        """
        SELECT
            asset_type,
            asset_value,
            first_seen
        FROM asset_inventory
        ORDER BY id DESC
        LIMIT 500
        """
    )
    print(dict(assets[0]))
    
    return render_template(
        "assets.html",
        assets=assets
    )


@app.route("/findings")
def findings():

    findings = query_all(
        """
        SELECT
            severity,
            score,
            title,
            evidence
        FROM findings
        ORDER BY score DESC
        """
    )

    return render_template(
        "findings.html",
        findings=findings
    )


@app.route("/screenshots")
def screenshots():

    screenshots = query_all(
        """
        SELECT
            host,
            image_path
        FROM screenshots
        ORDER BY id DESC
        """
    )

    return render_template(
        "screenshots.html",
        screenshots=screenshots
    )


@app.route("/image")
def image():

    path = request.args.get("path")

    absolute_path = (
        Path.cwd() / path
    )

    print(
        f"[IMAGE] {absolute_path}"
    )

    return send_file(
        absolute_path
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )