from pathlib import Path


class MarkdownReport:

    def generate(
        self,
        workspace,
        target,
        findings
    ):

        report = f"# AutoRec Report\n\n"

        report += f"## Target\n\n{target}\n\n"

        report += "## Findings\n\n"

        for finding in findings:

            report += (
                f"- [{finding['severity']}] "
                f"{finding['title']} "
                f"(Score: {finding['score']})\n"
            )

        report_file = (
            Path(workspace)
            / "report.md"
        )

        report_file.write_text(report)

        return report_file