from correlation.scorer import Scorer

class CorrelationEngine:

    def __init__(
        self,
        repository
    ):

        self.repository = repository

        self.scorer = Scorer()

    def analyze_url(
        self,
        url
    ):

        finding = (
            self.scorer.match(
                url
            )
        )

        if not finding:

            return

        self.repository.add_finding(
            finding["severity"],
            finding["score"],
            finding["title"],
            url
        )