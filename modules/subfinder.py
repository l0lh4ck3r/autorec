from pathlib import Path

from core.module import ReconModule
from core.toolrunner import ToolRunner


class SubfinderModule(ReconModule):

    name = "subfinder"

    dependencies = []

    async def run(self, context):

        print("[*] Running Subfinder")

        output_dir = (
            context.workspace
            / "subdomains"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        output_file = (
            output_dir
            / "subfinder.txt"
        )

        cmd = (
            f"subfinder "
            f"-d {context.target} "
            f"-silent "
            f"-o {output_file}"
        )

        result = await ToolRunner.run(cmd)

        print(
            f"[SUBFINDER] Return Code: "
            f"{result['returncode']}"
        )

        if result["stderr"]:

            print(
                f"[SUBFINDER ERROR]\n"
                f"{result['stderr']}"
            )

        # Store discovered assets
        if output_file.exists():

            hosts = (
                output_file
                .read_text()
                .splitlines()
            )

            for host in hosts:

                if context.repository:

                    context.repository.add_asset(
                        context.scan_id,
                        "subdomain",
                        host
                    )

        return result