class SearchEngine:

    def __init__(self, repository):

        self.repository = repository

    def search(self, keyword):

        keyword = f"%{keyword}%"

        findings = self.repository.db.fetchall(
            """
            SELECT
                severity,
                score,
                title,
                evidence
            FROM findings
            WHERE evidence LIKE ?
            """,
            (keyword,)
        )

        assets = self.repository.db.fetchall(
            """
            SELECT
                asset_type,
                asset_value
            FROM asset_inventory
            WHERE asset_value LIKE ?
            """,
            (keyword,)
        )

        urls = self.repository.db.fetchall(
            """
            SELECT url, source
            FROM url_inventory
            WHERE url LIKE ?
            """,
            (keyword,)
)

        return {
            "findings": findings,
            "assets": assets,
            "url": urls
        }