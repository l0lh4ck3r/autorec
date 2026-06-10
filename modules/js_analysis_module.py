import json
import re
import requests

from core.module import ReconModule


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

            lines = file.read_text(
                errors="ignore"
            ).splitlines()

            print(
                f"[JS] {file.name}: "
                f"{len(lines)} lines"
            )

            for line in lines:

                line = line.strip()

                # Temporary/simple detection
                if re.search(
                    r"\.(js|mjs)(\?|$)",
                    line,
                    re.IGNORECASE
                ):
                    js_urls.add(line)
                    js_urls.add(line)

        output_dir = (
            context.workspace
            / "js"
        )
        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        files_dir = (
            output_dir
            / "files"
        )

        files_dir.mkdir(
            exist_ok=True
        )

        js_url_file = (
            output_dir
            / "js_urls.txt"
        )

        print(
            f"[JS] Total URLs Found: "
            f"{len(js_urls)}"
        )

        js_url_file.write_text(
            "\n".join(sorted(js_urls)) + "\n"
        )

        print(
            f"[JS] Found {len(js_urls)} JavaScript files"
        )

        if js_urls:

            print(
                f"[JS] Saved -> {js_url_file}"
            )

            print("[JS] Sample URLs:")

            for url in sorted(js_urls)[:10]:

                print(
                f"[JS URL] {url}"
                )
            print(
                "[JS] Starting downloads..."
            )

            downloaded = 0

            for index, url in enumerate(
                sorted(js_urls)[:3]
            ):

                try:

                    print(
                        f"[JS] Downloading: {url}"
                    )

                    response = requests.get(
                        url,
                        timeout=15,
                        headers={
                            "User-Agent":
                            "AutoRec"
                        }
                    )

                    if response.status_code != 200:

                        print(
                            f"[JS] Skipped "
                            f"({response.status_code})"
                        )

                        continue

                    file_path = (
                        files_dir
                        / f"file_{index}.js"
                    )

                    file_path.write_text(
                        response.text
                    )

                    downloaded += 1

                    print(
                        f"[JS] Saved -> "
                        f"{file_path.name}"
                    )

                except Exception as e:

                    print(
                        f"[JS ERROR] {e}"
                    )

            print(
                f"[JS] Downloaded "
                f"{downloaded} files"
            )

        endpoints_file = (
            output_dir
            / "endpoints.jsonl"
        )

        endpoint_regex = re.compile(
            r'/(?:api|admin|v1|v2)[^"\']*'
        )

        with open(
            endpoints_file,
            "w"
        ) as out:

            for js_url in js_urls:

                findings = []

                for match in endpoint_regex.findall(
                    js_url
                ):

                    findings.append(
                        {
                            "source": js_url,
                            "endpoint": match
                        }
                    )

                for finding in findings:

                    out.write(
                        json.dumps(
                            finding
                        )
                        + "\n"
                    )

        print(
            "[JS] Endpoint extraction complete"
        )