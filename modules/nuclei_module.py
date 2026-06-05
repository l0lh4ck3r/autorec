import json
import subprocess


class NucleiModule:

    name = "nuclei"

    dependencies = [
        "httpx"
    ]

    async def run(
        self,
        context
    ):

        targets_file = (
            context.workspace
            / "http"
            / "alive_urls.txt"
        )

        output_file = (
            context.workspace
            / "nuclei.jsonl"
        )

        if not targets_file.exists():

            print(
                "[!] alive_hosts.txt not found"
            )

            return

        print(
            "[*] Running Nuclei..."
        )

        cmd = [
            "nuclei",
            "-l",
            str(targets_file),
            "-jsonl",
            "-silent",
            "-o",
            str(output_file)
        ]

        subprocess.run(
            cmd,
            check=False
        )

        if not output_file.exists():

            print(
                "[!] No Nuclei output generated"
            )

            return

        repo = context.repository

        score_map = {
            "critical": 100,
            "high": 75,
            "medium": 50,
            "low": 25,
            "info": 10
        }

        imported = 0

        with open(
            output_file,
            "r",
            encoding="utf-8"
        ) as f:

            for line in f:

                try:

                    result = json.loads(
                        line.strip()
                    )

                except Exception:

                    continue

                severity = (
                    result
                    .get(
                        "info",
                        {}
                    )
                    .get(
                        "severity",
                        "info"
                    )
                )

                title = (
                    result
                    .get(
                        "info",
                        {}
                    )
                    .get(
                        "name",
                        "Unknown Finding"
                    )
                )

                evidence = (
                    result.get(
                        "matched-at",
                        ""
                    )
                )

                score = score_map.get(
                    severity.lower(),
                    10
                )

                repo.add_finding(
                    severity,
                    score,
                    title,
                    evidence
                )

                imported += 1

        print(
            f"[+] Imported {imported} findings"
        )