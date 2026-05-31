from core.module import ReconModule
from core.toolrunner import ToolRunner

from correlation.engine import (
CorrelationEngine
)

class WaybackUrlsModule(ReconModule):

    name = "waybackurls"

    dependencies = ["subfinder"]

    async def run(self, context):

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
            / "waybackurls.txt"
        )

        cmd = (
            f"echo {context.target} "
            f"| waybackurls "
            f"> {output_file}"
        )

        result = await ToolRunner.run(cmd)

        if output_file.exists():

            urls = (
                output_file
                .read_text()
                .splitlines()
            )
            print(
                f"[WAYBACK] Collected {len(urls)} URLs"
            )

            engine = (
                CorrelationEngine(
                    context.repository
                )
            )

            imported = 0
            
            for url in urls:

                context.repository.add_discovered_url(
                    context.scan_id,
                    url,
                    "waybackurls"
                )
                imported += 1

                engine.analyze_url(url)

                print(
                    f"[WAYBACK] Imported {imported} URLs"
                )

                engine.analyze_url(
                    url
                )

        return result