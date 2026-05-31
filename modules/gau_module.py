from core.module import ReconModule
from core.toolrunner import ToolRunner

from correlation.engine import (
CorrelationEngine
)

class GauModule(ReconModule):

    name = "gau"

    dependencies = ["subfinder"]

    async def run(self, context):

        print("[*] Running GAU")

        output_dir = (
            context.workspace
            / "urls"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = (
            output_dir
            / "gau.txt"
        )

        cmd = (
            f"gau {context.target} "
            f"> {output_file}"
        )
        print("=" * 80)
        print("[HTTPX CMD]")
        print(cmd)
        print("=" * 80)

        which_result = await ToolRunner.run(
            "which httpx"
        )

        print(
            f"[HTTPX BIN] {which_result['stdout'].strip()}"
        )

        result = await ToolRunner.run(cmd)

        if output_file.exists():

            urls = (
                output_file
                .read_text()
                .splitlines()
            )

            print(
                f"[GAU] Collected {len(urls)} URLs"
            )

            engine = CorrelationEngine(
                context.repository
            )

            imported = 0

            for url in urls:

                context.repository.add_discovered_url(
                    context.scan_id,
                    url,
                    "gau"
                )

                imported += 1

                engine.analyze_url(url)

            print(
                f"[GAU] Imported {imported} URLs"
            )

            engine.analyze_url(
                    url
                )

        return result