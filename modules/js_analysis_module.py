import json
import re
import requests
import urllib3

from core.module import ReconModule

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class JavascriptAnalysisModule(ReconModule):
    name = "javascript"

    dependencies = [
        "gau",
    ]

    async def run(self, context):

        print("[*] Running JavaScript Analysis")

        urls_dir = context.workspace / "urls"

        gau_file = urls_dir / "gau.txt"
        wayback_file = urls_dir / "waybackurls.txt"

        js_urls = set()

        for file in [gau_file, wayback_file]:
            print(f"[JS] Reading: {file}")

            if not file.exists():
                print(f"[JS] Missing: {file}")
                continue

            lines = file.read_text(errors="ignore").splitlines()

            print(f"[JS] {file.name}: {len(lines)} lines")

            # Process only first 5000 lines while testing
            for line in lines[:5000]:
                line = line.strip()

                if re.search(r"\.(js|mjs)(\?|$)", line, re.IGNORECASE):
                    js_urls.add(line)

        output_dir = context.workspace / "js"

        output_dir.mkdir(parents=True, exist_ok=True)

        files_dir = output_dir / "files"

        files_dir.mkdir(exist_ok=True)

        js_url_file = output_dir / "js_urls.txt"

        print(f"[JS] Total URLs Found: {len(js_urls)}")

        js_url_file.write_text("\n".join(sorted(js_urls)) + "\n")

        print(f"[JS] Found {len(js_urls)} JavaScript files")

        if js_urls:
            print(f"[JS] Saved -> {js_url_file}")

            print("[JS] Sample URLs:")

            for url in sorted(js_urls)[:10]:
                print(f"[JS URL] {url}")

            print("[JS] Starting downloads...")

            downloaded = 0

            for index, url in enumerate(list(js_urls)[:3]):
                try:
                    print(f"[JS] Downloading: {url}")

                    response = requests.get(
                        url, timeout=15, verify=False, headers={"User-Agent": "AutoRec"}
                    )

                    print(f"[JS] Status: {response.status_code}")

                    if response.status_code != 200:
                        print(f"[JS] Skipped ({response.status_code})")

                        continue

                    file_path = files_dir / f"file_{index}.js"

                    file_path.write_text(response.text)

                    downloaded += 1

                    print(f"[JS] Saved -> {file_path.name}")

                except Exception as e:
                    print(f"[JS ERROR] {e}")

            print(f"[JS] Downloaded {downloaded} files")

            print(f"[JS] Files directory: {files_dir}")

            print("[JS] Extracting endpoints...")

            endpoint_regex = re.compile(
                r'/(?:api|rest|graphql|admin|auth|login)[^"\']*', re.IGNORECASE
            )

            endpoints_file = output_dir / "endpoints.jsonl"

            endpoint_count = 0

            with open(endpoints_file, "w") as out:
                for js_file in files_dir.glob("*.js"):
                    try:
                        content = js_file.read_text(errors="ignore")

                        matches = set(endpoint_regex.findall(content))

                        for endpoint in matches:
                            finding = {"file": js_file.name, "endpoint": endpoint}

                            out.write(json.dumps(finding) + "\n")

                            endpoint_count += 1

                    except Exception as e:
                        print(f"[JS ERROR] {e}")

            print(f"[JS] Found {endpoint_count} endpoints")

            print(f"[JS] Saved -> {endpoints_file}")

            for js_file in files_dir.glob("*.js"):
                try:
                    content = js_file.read_text(errors="ignore")

                    print(f"[JS] {js_file.name}: {len(content)} bytes")

                except Exception as e:
                    print(f"[JS ERROR] {e}")
                print("[JS] Detecting secrets...")

        secrets_file = output_dir / "secrets.jsonl"

        secret_patterns = {
            "api_key": r"api[_-]?key",
            "token": r"token",
            "secret": r"secret",
            "password": r"password",
            "bearer": r"bearer",
            "jwt": r"eyJ[A-Za-z0-9_-]+",
        }

        secret_count = 0

        with open(secrets_file, "w") as out:
            for js_file in files_dir.glob("*.js"):
                try:
                    content = js_file.read_text(errors="ignore")

                    for name, pattern in secret_patterns.items():
                        matches = re.findall(pattern, content, re.IGNORECASE)

                        if matches:
                            finding = {
                                "file": js_file.name,
                                "type": name,
                                "count": len(matches),
                            }

                            out.write(json.dumps(finding) + "\n")

                            secret_count += 1

                except Exception as e:
                    print(f"[JS ERROR] {e}")

        print(f"[JS] Found {secret_count} secret indicators")

        print(f"[JS] Saved -> {secrets_file}")

        endpoints_file = output_dir / "endpoints.jsonl"

        endpoint_regex = re.compile(r'/(?:api|admin|v1|v2)[^"\']*')

        with open(endpoints_file, "w") as out:
            for js_url in js_urls:
                findings = []

                for match in endpoint_regex.findall(js_url):
                    findings.append({"source": js_url, "endpoint": match})

                for finding in findings:
                    out.write(json.dumps(finding) + "\n")

        print("[JS] Endpoint extraction complete")
