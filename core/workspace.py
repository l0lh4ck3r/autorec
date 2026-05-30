from pathlib import Path
from datetime import datetime


class Workspace:

    def create(self, target):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        path = (
            Path("output")
            / f"{target}_{timestamp}"
        )

        path.mkdir(
            parents=True,
            exist_ok=True
        )

        return path
