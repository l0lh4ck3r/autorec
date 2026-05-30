from core.module import ReconModule
from core.toolrunner import ToolRunner


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

        result = await ToolRunner.run(cmd)

        if output_file.exists():

            urls = (
                output_file
                .read_text()
                .splitlines()
            )

            for url in urls:

                context.repository.add_discovered_url(
                    context.scan_id,
                    url,
                    "gau"
                )

        return result