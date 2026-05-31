from correlation.rules import RULES

class Scorer:

    def match(self, text):

        text = text.lower()

        for keyword, data in RULES.items():

            if keyword.lower() in text:

                return data

        return None

    def score(self, text):

        finding = self.match(text)

        if not finding:
            return 0

        return finding["score"]

    def severity(self, score):

        if score >= 90:
            return "Critical"

        if score >= 70:
            return "High"

        if score >= 40:
            return "Medium"

        return "Low"
