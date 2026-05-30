from pathlib import Path

from jinja2 import (
    Environment,
    FileSystemLoader
)


class HTMLReport:

    def generate(
        self,
        workspace,
        target,
        findings
    ):

        env = Environment(
            loader=
            FileSystemLoader(
                "templates"
            )
        )

        template = env.get_template(
            "report.html"
        )

        html = template.render(
            target=target,
            findings=findings
        )

        report_file = (
            Path(workspace)
            / "report.html"
        )

        report_file.write_text(
            html
        )

        return report_file