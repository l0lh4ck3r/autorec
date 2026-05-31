from pathlib import Path
import shutil

from jinja2 import (
Environment,
FileSystemLoader
)

class HTMLReport:

    def generate(
        self,
        workspace,
        target,
        findings,
        screenshots,
        assets=None,
        technologies=None,
        stats=None
    ):

        workspace = Path(workspace)

        dashboard_screenshots = (
            workspace
            / "screenshots"
        )

        dashboard_screenshots.mkdir(
            exist_ok=True
        )

        normalized_screenshots = []

        for shot in screenshots:

            image_path = (
                shot["image_path"]
            )

            image_file = Path(
                image_path
            )

            if image_file.exists():

                destination = (
                    dashboard_screenshots
                    / image_file.name
                )

                if not destination.exists():

                    shutil.copy2(
                        image_file,
                        destination
                    )

                shot = dict(shot)

                shot["image_path"] = (
                    f"screenshots/{image_file.name}"
                )

            normalized_screenshots.append(
                shot
            )

        env = Environment(
            loader=FileSystemLoader(
                "templates"
            )
        )

        template = env.get_template(
            "report.html"
        )

        html = template.render(
            target=target,
            findings=findings,
            screenshots=normalized_screenshots,
            assets=assets or [],
            technologies=technologies or [],
            stats=stats or {}
        )

        report_file = (
            workspace
            / "report.html"
        )

        report_file.write_text(
            html,
            encoding="utf-8"
        )

        return report_file