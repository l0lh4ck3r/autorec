import json

from core.module import ReconModule


class InterestingMapperModule(ReconModule):
    name = "interesting_mapper"

    dependencies = ["auth_mapper"]

    async def run(self, context):

        print("[*] Running Interesting Mapper")

        urls_dir = context.workspace / "urls"

        auth_dir = context.workspace / "auth"

        js_dir = context.workspace / "js"

        files = [
            urls_dir / "gau.txt",
            urls_dir / "waybackurls.txt",
            auth_dir / "auth_findings.jsonl",
            js_dir / "endpoints.jsonl",
        ]

        interesting_patterns = [
            "admin",
            "graphql",
            "swagger",
            "api-docs",
            "openapi",
            "debug",
            "actuator",
            "metrics",
            "health",
            "console",
            "phpinfo",
            "jenkins",
            "kibana",
            "prometheus",
            "dashboard",
        ]

        output_dir = context.workspace / "interesting"

        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "findings.jsonl"

        findings = []
        seen = set()

        for file in files:
            if not file.exists():
                continue

            print(f"[INT] Reading: {file}")

            for line in file.read_text(errors="ignore").splitlines():
                lower = line.lower()

                for pattern in interesting_patterns:
                    if pattern in lower:
                        key = (pattern, line)

                        if key in seen:
                            break

                        seen.add(key)

                        findings.append(
                            {"type": pattern, "source": file.name, "value": line}
                        )

                        break

        with open(output_file, "w") as out:
            for finding in findings:
                out.write(json.dumps(finding) + "\n")

        print(f"[INT] Found {len(findings)} interesting endpoints")

        print(f"[INT] Saved -> {output_file}")

        print("[INT] Sample Findings:")

        for finding in findings[:10]:
            print(f"[INT] {finding['type']} -> {finding['source']}")
