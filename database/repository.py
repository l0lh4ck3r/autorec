from datetime import datetime


class Repository:

    def __init__(self, db):
        self.db = db

    # -------------------------
    # SCANS
    # -------------------------

    def create_scan(
        self,
        target,
        profile
    ):

        now = datetime.utcnow().isoformat()

        cursor = self.db.execute(
            """
            INSERT INTO scans(
                target,
                profile,
                status,
                started_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                target,
                profile,
                "running",
                now
            )
        )

        return cursor.lastrowid

    def complete_scan(
        self,
        scan_id
    ):

        now = datetime.utcnow().isoformat()

        self.db.execute(
            """
            UPDATE scans
            SET status = ?,
                completed_at = ?
            WHERE id = ?
            """,
            (
                "completed",
                now,
                scan_id
            )
        )

    # -------------------------
    # HOSTS
    # -------------------------

    def add_host(
        self,
        scan_id,
        hostname,
        ip=None
    ):

        self.db.execute(
            """
            INSERT INTO hosts(
                scan_id,
                hostname,
                ip
            )
            VALUES (?, ?, ?)
            """,
            (
                scan_id,
                hostname,
                ip
            )
        )

    # -------------------------
    # URLS
    # -------------------------

    def add_url(
        self,
        url,
        status_code=None
    ):

        self.db.execute(
            """
            INSERT INTO urls(
                url,
                status_code
            )
            VALUES (?, ?)
            """,
            (
                url,
                status_code
            )
        )

    # -------------------------
    # FINDINGS
    # -------------------------

    def add_finding(
        self,
        severity,
        score,
        title,
        evidence
    ):

        now = datetime.utcnow().isoformat()

        self.db.execute(
            """
            INSERT INTO findings(
                severity,
                score,
                title,
                evidence,
                created_at
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                severity,
                score,
                title,
                evidence,
                now
            )
        )

    def get_findings(self):

        return self.db.fetchall(
            """
            SELECT *
            FROM findings
            ORDER BY score DESC
            """
        )

    # -------------------------
    # ASSETS
    # -------------------------

    def add_asset(
        self,
        scan_id,
        asset_type,
        asset_value
    ):

        now = datetime.utcnow().isoformat()

        self.db.execute(
            """
            INSERT INTO asset_inventory(
                scan_id,
                asset_type,
                asset_value,
                first_seen,
                last_seen
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                scan_id,
                asset_type,
                asset_value,
                now,
                now
            )
        )

    def get_assets(self):

        return self.db.fetchall(
            """
            SELECT *
            FROM asset_inventory
            ORDER BY asset_type
            """
        )

    # -------------------------
    # TECHNOLOGIES
    # -------------------------

    def add_technology(
        self,
        host,
        technology
    ):

        self.db.execute(
            """
            INSERT INTO technologies(
                host,
                technology
            )
            VALUES (?, ?)
            """,
            (
                host,
                technology
            )
        )
    # -------------------------
    # SCAN HELPERS
    # -------------------------

    def get_latest_scan(self):

        result = self.db.fetchone(
            """
            SELECT *
            FROM scans
            ORDER BY id DESC
            LIMIT 1
            """
        )
    def add_discovered_url(
        self,
        scan_id,
        url,
        source
    ):

        now = datetime.utcnow().isoformat()

        self.db.execute(
            """
            INSERT INTO url_inventory(
                scan_id,
                url,
                source,
                discovered_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                scan_id,
                url,
                source,
                now
            )
        )
    def get_urls(self):

        return self.db.fetchall(
            """
            SELECT *
            FROM url_inventory
            """
        )
    def add_technology(
        self,
        scan_id,
        host,
        technology
    ): 

        self.db.execute(
            """
            INSERT INTO technologies(
                scan_id,
                host,
                technology
            )
            VALUES (?, ?, ?)
            """,
            (
                scan_id,
                host,
                technology
            )
        )
        return result