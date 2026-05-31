import asyncio
import shutil
import typer

from cli.diff import DiffEngine
from database.db import Database
from cli.search import SearchEngine

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
        repo.get_findings(),
        repo.get_screenshots()
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


@app.command()
def search(
    keyword: str
):

    db = Database(
        "latest.db"
    )

    repo = Repository(
        db
    )

    engine = SearchEngine(
        repo
    )

    results = engine.search(
        keyword
    )

    print()

    print("=" * 50)
    print("ASSETS")
    print("=" * 50)

    for row in results.get("assets", []):

        print(
            f"{row['asset_type']}: "
            f"{row['asset_value']}"
        )

    print()

    print("=" * 50)
    print("FINDINGS")
    print("=" * 50)

    for row in results.get("findings", []):

        print(
            f"[{row['severity']}] "
            f"{row['evidence']}"
        )

    print()

    print("=" * 50)
    print("URLS")
    print("=" * 50)

    for row in results.get("urls", []):

        print(
            f"{row['source']} "
            f"{row['url']}"
        )

    print()

    print("=" * 50)
    print("TECHNOLOGIES")
    print("=" * 50)

    for row in results.get("technologies", []):

        print(
            f"{row['technology']} "
            f"-> "
            f"{row['host']}"
        )


@app.command()
def diff():

    db = Database(
        "latest.db"
    )

    repo = Repository(
        db
    )

    engine = DiffEngine(
        repo
    )

    print()

    print("=" * 50)
    print("NEW ASSETS")
    print("=" * 50)

    assets = engine.new_assets()

    if not assets:

        print("No differences found")

    else:

        for asset in assets:

            print(asset)

    print()

    print("=" * 50)
    print("NEW URLS")
    print("=" * 50)

    urls = engine.new_urls()

    if not urls:

        print("No new URLs")

    else:

        for url in urls:

            print(url)

    print()

    print("=" * 50)
    print("NEW TECHNOLOGIES")
    print("=" * 50)

    technologies = engine.new_technologies()

    if not technologies:

        print("No new technologies")

    else:

        for tech in technologies:

            print(tech)


if __name__ == "__main__":

    app()