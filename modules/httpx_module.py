from core.module import ReconModule
from core.toolrunner import ToolRunner

from correlation.scorer import Scorer


class HttpxModule(ReconModule):

    name = "httpx"

    dependencies = ["dnsx"]

    async def run(self, context):

        print("[*] Running HTTPX")

        http_dir = (
            context.workspace
            / "http"
        )

        http_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        input_file = (
            context.workspace
            / "dns"
            / "resolved.txt"
        )

        output_file = (
            http_dir
            / "alive_urls.txt"
        )
        urls_only_file = (
            http_dir
            / "alive_urls.txt"
        )

        if not input_file.exists():

            print(
                f"[HTTPX] Missing input file: "
                f"{input_file}"
            )

            return

        cmd = (
            f"httpx "
            f"-l {input_file} "
            f"-silent "
            f"-title "
            f"-tech-detect "
            f"-status-code "
            f"-follow-redirects "
            f"-o {output_file}"
        )

        result = await ToolRunner.run(cmd)

        print(
            f"[HTTPX] Return Code: "
            f"{result['returncode']}"
        )

        if result["stderr"]:

            print(
                f"[HTTPX ERROR]\n"
                f"{result['stderr']}"
            )

        scorer = Scorer()

        if output_file.exists():

            lines = (
                output_file
                .read_text()
                .splitlines()
            )
            clean_urls = []

            for line in lines:
                host = line.split()[0]

                clean_urls.append(host)

                if "[" in line and "]" in line:

                    try:

                        parts = line.split("[")

                        host = parts[0].strip()

                        tech_string = (
                            parts[-1]
                            .replace("]", "")
                            .strip()
                        )

                        technologies = [
                            x.strip()
                            for x in tech_string.split(",")
                        ]

                        for tech in technologies:

                            if tech:

                                context.repository.add_technology(
                                context.scan_id,
                                host,
                                tech
                            )

                    except Exception:

                        pass

                # Store asset
                if context.repository:

                    context.repository.add_asset(
                        context.scan_id,
                        "http_service",
                        line
                    )

                # Score finding
                score = scorer.score(line)

                severity = scorer.severity(
                    score
                )

                if score > 0:

                    print(
                        f"[FINDING] "
                        f"{severity} "
                        f"({score}) "
                        f"{line}"
                    )

                    if context.repository:

                        context.repository.add_finding(
                            severity=severity,
                            score=score,
                            title="Interesting Asset",
                            evidence=line
                        )
                        urls_only_file.write_text(
                        "\n".join(clean_urls)
                        )

        return result