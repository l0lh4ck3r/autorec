import asyncio
import shutil

import typer

from core.workspace import Workspace
from core.eventbus import EventBus
from core.context import ScanContext
from core.engine import Engine

from database.init_db import initialize_database
from database.repository import Repository

from cli.scan import load_modules
from cli.doctor import doctor

from reporting.html_report import HTMLReport


app = typer.Typer()


@app.command()
def scan(
    target: str,
    profile: str = "quick"
):
    asyncio.run(
        run_scan(
            target,
            profile
        )
    )


async def run_scan(
    target,
    profile
):

    workspace = Workspace()

    scan_dir = workspace.create(
        target
    )

    db = initialize_database(
        scan_dir / "scan.db"
    )

    repo = Repository(db)

    scan_id = repo.create_scan(
        target,
        profile
    )

    context = ScanContext(
        target=target,
        profile=profile,
        workspace=scan_dir,
        repository=repo,
        eventbus=EventBus(),
        scan_id=scan_id
    )

    modules = load_modules(
        profile
    )

    engine = Engine(
        modules
    )

    await engine.run(
        context
    )

    repo.complete_scan(
        scan_id
    )

    reporter = HTMLReport()

    reporter.generate(
        scan_dir,
        target,
        repo.get_findings()
    )

    shutil.copy(
        scan_dir / "scan.db",
        "latest.db"
    )

    print(
        f"[+] Scan completed: {scan_id}"
    )

    print(
        f"[+] Workspace: {scan_dir}"
    )


@app.command()
def doctor_cmd():

    doctor()


if __name__ == "__main__":

    app()