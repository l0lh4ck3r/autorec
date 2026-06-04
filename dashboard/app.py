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


def query_all(
    sql,
    params=()
):

    conn = sqlite3.connect(DB_FILE)

    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute(
        sql,
        params
    )

    rows = cur.fetchall()

    conn.close()

    return rows


@app.route("/")
def index():

    stats = {

        "assets": query_one(
            "SELECT COUNT(*) FROM asset_inventory"
        ),

        "urls": query_one(
            "SELECT COUNT(*) FROM url_inventory"
        ),

        "findings": query_one(
            "SELECT COUNT(*) FROM findings"
        ),

        "technologies": query_one(
            "SELECT COUNT(*) FROM technologies"
        ),

        "screenshots": query_one(
            "SELECT COUNT(*) FROM screenshots"
        ),

        "scans": query_one(
            "SELECT COUNT(*) FROM scans"
        )
    }

    asset_chart = query_all(
        """
        SELECT
            asset_type,
            COUNT(*) AS count
        FROM asset_inventory
        GROUP BY asset_type
        """
    )

    finding_chart = query_all(
        """
        SELECT
            severity,
            COUNT(*) AS count
        FROM findings
        GROUP BY severity
        """
    )

    technology_chart = query_all(
        """
        SELECT
            technology,
            COUNT(*) AS count
        FROM technologies
        GROUP BY technology
        ORDER BY count DESC
        LIMIT 10
        """
    )

    return render_template(
        "index.html",
        stats=stats,
        asset_chart=asset_chart,
        finding_chart=finding_chart,
        technology_chart=technology_chart
    )

@app.route("/assets")
def assets():

    asset_type = request.args.get(
        "type",
        ""
    )

    sort = request.args.get(
        "sort",
        "newest"
    )

    if sort == "oldest":

        order_by = "id ASC"

    elif sort == "type":

        order_by = "asset_type ASC"

    else:

        order_by = "id DESC"

    if asset_type:

        assets = query_all(
            f"""
            SELECT
                asset_type,
                asset_value,
                first_seen
            FROM asset_inventory
            WHERE asset_type = ?
            ORDER BY {order_by}
            LIMIT 1000
            """,
            (
                asset_type,
            )
        )

    else:

        assets = query_all(
            f"""
            SELECT
                asset_type,
                asset_value,
                first_seen
            FROM asset_inventory
            ORDER BY {order_by}
            LIMIT 1000
            """
        )

    return render_template(
        "assets.html",
        assets=assets,
        selected_type=asset_type,
        selected_sort=sort
    )

@app.route("/findings")
def findings():

    severity = request.args.get(
        "severity",
        ""
    )

    sort = request.args.get(
        "sort",
        "high"
    )

    if sort == "low":

        order_by = "score ASC"

    elif sort == "severity":

        order_by = "severity ASC"

    else:

        order_by = "score DESC"

    if severity:

        findings = query_all(
            f"""
            SELECT
                severity,
                score,
                title,
                evidence
            FROM findings
            WHERE severity = ?
            ORDER BY {order_by}
            """,
            (
                severity,
            )
        )

    else:

        findings = query_all(
            f"""
            SELECT
                severity,
                score,
                title,
                evidence
            FROM findings
            ORDER BY {order_by}
            """
        )

    return render_template(
        "findings.html",
        findings=findings,
        selected_severity=severity,
        selected_sort=sort
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

    return send_file(
        absolute_path
    )


@app.route("/urls")
def urls():

    source = request.args.get(
        "source",
        ""
    )

    sort = request.args.get(
        "sort",
        "newest"
    )

    page = int(
        request.args.get(
            "page",
            1
        )
    )

    per_page = 100

    offset = (
        page - 1
    ) * per_page

    if sort == "oldest":

        order_by = "discovered_at ASC"

    elif sort == "source":

        order_by = "source ASC"

    else:

        order_by = "discovered_at DESC"

    if source:

        urls = query_all(
            f"""
            SELECT
                url,
                source,
                discovered_at
            FROM url_inventory
            WHERE source = ?
            ORDER BY {order_by}
            LIMIT ?
            OFFSET ?
            """,
            (
                source,
                per_page,
                offset
            )
        )

        total_urls = len(
            query_all(
                """
                SELECT url
                FROM url_inventory
                WHERE source = ?
                """,
                (
                    source,
                )
            )
        )

    else:

        urls = query_all(
            f"""
            SELECT
                url,
                source,
                discovered_at
            FROM url_inventory
            ORDER BY {order_by}
            LIMIT ?
            OFFSET ?
            """,
            (
                per_page,
                offset
            )
        )

        total_urls = query_one(
            "SELECT COUNT(*) FROM url_inventory"
        )

    total_pages = (
        total_urls + per_page - 1
    ) // per_page

    return render_template(
        "urls.html",
        urls=urls,
        page=page,
        total_pages=total_pages,
        selected_source=source,
        selected_sort=sort
    )


@app.route("/technologies")
def technologies():

    technology = request.args.get(
        "technology",
        ""
    )

    sort = request.args.get(
        "sort",
        "technology"
    )

    if sort == "host":

        order_by = "host ASC"

    else:

        order_by = "technology ASC"

    if technology:

        technologies = query_all(
            f"""
            SELECT
                host,
                technology
            FROM technologies
            WHERE technology = ?
            ORDER BY {order_by}
            """,
            (
                technology,
            )
        )

    else:

        technologies = query_all(
            f"""
            SELECT
                host,
                technology
            FROM technologies
            ORDER BY {order_by}
            """
        )

    return render_template(
        "technologies.html",
        technologies=technologies,
        selected_technology=technology,
        selected_sort=sort
    )


@app.route("/scans")
def scans():

    scans = query_all(
        """
        SELECT
            target,
            profile,
            status,
            started_at,
            completed_at
        FROM scans
        ORDER BY started_at DESC
        """
    )

    return render_template(
        "scans.html",
        scans=scans
    )

@app.route("/search")
def search():

    q = request.args.get(
        "q",
        ""
    )

    like = f"%{q}%"

    assets = query_all(
        """
        SELECT *
        FROM asset_inventory
        WHERE asset_value LIKE ?
        LIMIT 100
        """,
        (
            like,
        )
    )

    urls = query_all(
        """
        SELECT *
        FROM url_inventory
        WHERE url LIKE ?
        LIMIT 100
        """,
        (
            like,
        )
    )

    technologies = query_all(
        """
        SELECT *
        FROM technologies
        WHERE technology LIKE ?
           OR host LIKE ?
        LIMIT 100
        """,
        (
            like,
            like
        )
    )

    findings = query_all(
        """
        SELECT *
        FROM findings
        WHERE title LIKE ?
           OR evidence LIKE ?
        LIMIT 100
        """,
        (
            like,
            like
        )
    )

    return render_template(
        "search.html",
        q=q,
        assets=assets,
        urls=urls,
        technologies=technologies,
        findings=findings
    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )