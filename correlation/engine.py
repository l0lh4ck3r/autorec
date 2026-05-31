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

        score = (
            self.scorer.score(
                url
            )
        )

        if score <= 0:

            return

        severity = (
            self.scorer.severity(
                score
            )
        )

        self.repository.add_finding(
            severity,
            score,
            "Interesting URL Detected",
            url
        )