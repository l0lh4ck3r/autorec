from pathlib import Path


def latest_workspace():

    dirs = list(
        Path("output").glob("*")
    )

    dirs.sort()

    return dirs[-1]


def generate_report():

    workspace = latest_workspace()

    report_file = (
        workspace
        / "report.md"
    )

    print(
        f"Report: {report_file}"
    )