class DiffEngine:

    def __init__(
        self,
        repository
    ):
        self.repository = repository

    def asset_count(self):

        result = self.repository.db.fetchone(
            """
            SELECT COUNT(*)
            AS total
            FROM asset_inventory
            """
        )

        return result["total"]

    def url_count(self):

        result = self.repository.db.fetchone(
            """
            SELECT COUNT(*)
            AS total
            FROM url_inventory
            """
        )

        return result["total"]