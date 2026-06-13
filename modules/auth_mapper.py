import json

from core.module import ReconModule


class AuthMapperModule(ReconModule):
    name = "auth_mapper"

    dependencies = [
        "gau",
    ]

    async def run(self, context):

        print("[*] Running Auth Mapper")

        urls_dir = context.workspace / "urls"

        files = [urls_dir / "gau.txt", urls_dir / "waybackurls.txt"]

        auth_keywords = [
            "login",
            "signin",
            "signup",
            "register",
            "auth",
            "oauth",
            "forgot-password",
            "forgotpassword",
            "reset-password",
            "resetpassword",
            "sso",
            "token",
            "jwt",
            "account",
        ]

        output_dir = context.workspace / "auth"

        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / "auth_findings.jsonl"

        findings = []
        seen = set()

        for file in files:
            if not file.exists():
                print(f"[AUTH] Missing: {file}")

                continue

            print(f"[AUTH] Reading: {file}")

            for line in file.read_text(errors="ignore").splitlines():
                url = line.strip()

                if not url:
                    continue

                url_lower = url.lower()

                for keyword in auth_keywords:
                    if keyword in url_lower:
                        key = (keyword, url)

                        if key in seen:
                            break

                        seen.add(key)

                        findings.append({"type": keyword, "url": url})

                        break

        with open(output_file, "w") as out:
            for finding in findings:
                out.write(json.dumps(finding) + "\n")

        print(f"[AUTH] Found {len(findings)} authentication URLs")

        print(f"[AUTH] Saved -> {output_file}")

        print("[AUTH] Sample Findings:")

        for finding in findings[:10]:
            print(f"[AUTH] {finding['type']} -> {finding['url']}")
