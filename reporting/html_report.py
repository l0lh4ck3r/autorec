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
        findings,
        screenshots,
        assets=None,
        technologies=None,
        stats=None
    ):
    
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
            screenshots=screenshots,
            assets=assets or [],
            technologies=technologies or [],
            stats=stats or {}
        )
    
        report_file = (
            Path(workspace)
            / "report.html"
        )
    
        report_file.write_text(
            html,
            encoding="utf-8"
        )
    
        return report_file