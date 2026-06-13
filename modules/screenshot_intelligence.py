import json

from core.module import ReconModule


class ScreenshotIntelligenceModule(ReconModule):
    name = "screenshot_intelligence"

    dependencies = ["gowitness"]

    async def run(self, context):

        print("[*] Running Screenshot Intelligence")

        screenshots_dir = context.workspace / "screenshots"

        output_dir = context.workspace / "intelligence"

        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "screenshots.jsonl"

        patterns = {
            "cpanel": "hosting_panel",
            "webmail": "webmail",
            "mail": "mail_server",
            "admin": "admin_panel",
            "dashboard": "dashboard",
            "grafana": "grafana",
            "jenkins": "jenkins",
            "kibana": "kibana",
            "prometheus": "prometheus",
            "phpmyadmin": "phpmyadmin",
        }

        findings = []
        seen = set()

        for image in screenshots_dir.glob("*.jpeg"):
            name = image.name.lower()

            for keyword, finding_type in patterns.items():
                if keyword in name:
                    if image.name in seen:
                        break

                    seen.add(image.name)

                    findings.append({"type": finding_type, "screenshot": image.name})

                    break

        with open(output_file, "w") as out:
            for finding in findings:
                out.write(json.dumps(finding) + "\n")

        print(f"[SHOT] Found {len(findings)} interesting screenshots")

        print(f"[SHOT] Saved -> {output_file}")

        for finding in findings[:10]:
            print(f"[SHOT] {finding['type']} -> {finding['screenshot']}")
