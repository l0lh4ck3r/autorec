from correlation.rules import RULES


class Scorer:

    def score(self, text):

        total = 0

        text = text.lower()

        for keyword, points in RULES.items():

            if keyword.lower() in text:

                total += points

        return total

    def severity(self, score):

        if score >= 90:
            return "Critical"

        if score >= 70:
            return "High"

        if score >= 40:
            return "Medium"

        return "Low"