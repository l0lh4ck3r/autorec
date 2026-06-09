import json
import re

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

            if not file.exists():
                continue

            for line in file.read_text(
                errors="ignore"
            ).splitlines():

                line = line.strip()

                if (
                    ".js" in line
                    or ".mjs" in line
                ):
                    js_urls.add(line)

        output_dir = (
            context.workspace
            / "js"
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        js_url_file = (
            output_dir
            / "js_urls.txt"
        )

        js_url_file.write_text(
            "\n".join(sorted(js_urls))
        )

        print(
            f"[JS] Found {len(js_urls)} JavaScript files"
        )
        if js_urls:

            print(
                f"[JS] Saved -> {js_url_file}"
            )

            for url in sorted(js_urls)[:10]:

                print(
                    f"[JS URL] {url}"
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