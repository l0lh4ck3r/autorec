class DiffEngine:

    def __init__(self, repository):

        self.repository = repository

    def latest_scan_id(self):

        row = self.repository.db.fetchone(
            """
            SELECT id
            FROM scans
            ORDER BY id DESC
            LIMIT 1
            """
        )

        if not row:
            return None

        return row["id"]

    def previous_scan_id(self):

        row = self.repository.db.fetchone(
            """
            SELECT id
            FROM scans
            ORDER BY id DESC
            LIMIT 1 OFFSET 1
            """
        )

        if not row:
            return None

        return row["id"]

    def new_assets(self):

        latest = self.latest_scan_id()

        previous = self.previous_scan_id()

        if not latest or not previous:
            return []

        latest_assets = self.repository.db.fetchall(
            """
            SELECT asset_value
            FROM asset_inventory
            WHERE scan_id = ?
            """,
            (latest,)
        )

        previous_assets = self.repository.db.fetchall(
            """
            SELECT asset_value
            FROM asset_inventory
            WHERE scan_id = ?
            """,
            (previous,)
        )

        latest_set = {
            row["asset_value"]
            for row in latest_assets
        }

        previous_set = {
            row["asset_value"]
            for row in previous_assets
        }

        return sorted(
            latest_set - previous_set
        )

    def new_urls(self):

        latest = self.latest_scan_id()

        previous = self.previous_scan_id()

        if not latest or not previous:
            return []

        latest_urls = self.repository.db.fetchall(
            """
            SELECT url
            FROM url_inventory
            WHERE scan_id = ?
            """,
            (latest,)
        )

        previous_urls = self.repository.db.fetchall(
            """
            SELECT url
            FROM url_inventory
            WHERE scan_id = ?
            """,
            (previous,)
        )

        latest_set = {
            row["url"]
            for row in latest_urls
        }

        previous_set = {
            row["url"]
            for row in previous_urls
        }

        return sorted(
            latest_set - previous_set
        )

    def new_technologies(self):

        latest = self.latest_scan_id()

        previous = self.previous_scan_id()

        if not latest or not previous:
            return []

        latest_tech = self.repository.db.fetchall(
            """
            SELECT technology
            FROM technologies
            WHERE scan_id = ?
            """,
            (latest,)
        )

        previous_tech = self.repository.db.fetchall(
            """
            SELECT technology
            FROM technologies
            WHERE scan_id = ?
            """,
            (previous,)
        )

        latest_set = {
            row["technology"]
            for row in latest_tech
        }

        previous_set = {
            row["technology"]
            for row in previous_tech
        }

        return sorted(
            latest_set - previous_set
        )