import json

from core.module import ReconModule


class PrioritizationModule(ReconModule):
    name = "prioritization"

    dependencies = ["interesting_mapper"]

    async def run(self, context):

        print("[*] Running Prioritization Engine")

        output_dir = context.workspace / "priority"

        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "findings.jsonl"

        findings = []

        #
        # Interesting Endpoints
        #

        interesting_file = context.workspace / "interesting" / "findings.jsonl"

        if interesting_file.exists():
            for line in interesting_file.read_text(errors="ignore").splitlines():
                try:
                    item = json.loads(line)

                    score = 20

                    if item.get("type") == "admin":
                        score = 50

                    findings.append(
                        {
                            "source": "interesting",
                            "type": item.get("type"),
                            "score": score,
                        }
                    )

                except Exception:
                    pass

        #
        # Auth Findings
        #

        auth_file = context.workspace / "auth" / "auth_findings.jsonl"

        if auth_file.exists():
            for line in auth_file.read_text(errors="ignore").splitlines():
                try:
                    item = json.loads(line)

                    findings.append(
                        {"source": "auth", "type": item.get("type"), "score": 10}
                    )

                except Exception:
                    pass

        #
        # Secret Findings
        #

        secrets_file = context.workspace / "js" / "secrets.jsonl"

        if secrets_file.exists():
            for line in secrets_file.read_text(errors="ignore").splitlines():
                try:
                    item = json.loads(line)

                    findings.append(
                        {"source": "secret", "type": item.get("type"), "score": 30}
                    )

                except Exception:
                    pass

        #
        # Priority Calculation
        #

        for finding in findings:
            score = finding["score"]

            if score >= 90:
                priority = "HIGH"

            elif score >= 50:
                priority = "MEDIUM"

            else:
                priority = "LOW"

            finding["priority"] = priority

        #
        # Save
        #

        with open(output_file, "w") as out:
            for finding in findings:
                out.write(json.dumps(finding) + "\n")

        print(f"[PRIORITY] {len(findings)} findings scored")

        print(f"[PRIORITY] Saved -> {output_file}")
