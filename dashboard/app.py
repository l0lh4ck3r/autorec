from flask import Flask, render_template
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


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )