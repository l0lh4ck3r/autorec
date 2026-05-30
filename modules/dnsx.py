from core.module import ReconModule
from core.toolrunner import ToolRunner


class DnsxModule(ReconModule):

    name = "dnsx"

    dependencies = ["subfinder"]

    async def run(self, context):

        print("[*] Running DNSX")

        dns_dir = (
            context.workspace
            / "dns"
        )

        dns_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        input_file = (
            context.workspace
            / "subdomains"
            / "subfinder.txt"
        )

        output_file = (
            dns_dir
            / "resolved.txt"
        )

        if not input_file.exists():

            print(
                f"[DNSX] Missing input file: "
                f"{input_file}"
            )

            return

        cmd = (
            f"dnsx "
            f"-l {input_file} "
            f"-silent "
            f"-o {output_file}"
        )

        result = await ToolRunner.run(cmd)

        print(
            f"[DNSX] Return Code: "
            f"{result['returncode']}"
        )

        if result["stderr"]:

            print(
                f"[DNSX ERROR]\n"
                f"{result['stderr']}"
            )

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
                        "resolved_host",
                        host
                    )

        return result