---
name: Custom issue template
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

# Customization Guide

This document explains how to customize AutoRec for your own reconnaissance workflows.

---

# Profiles

Profiles control which modules are executed during a scan.

Configuration file:

```text
config/profiles.yaml
```

Example:

```yaml
profiles:

  quick:
    modules:
      - subfinder
      - dnsx
      - httpx

  full:
    modules:
      - subfinder
      - dnsx
      - httpx
      - gau
      - javascript
      - auth_mapper
      - interesting_mapper
      - nuclei
```

Run:

```bash
python autorec.py scan example.com --profile quick
```

---

# Adding New Modules

Create a module:

```text
modules/my_module.py
```

Example:

```python
from core.module import ReconModule


class MyModule(ReconModule):

    name = "my_module"

    dependencies = [
        "httpx"
    ]

    async def run(self, context):

        print(
            "[*] Running My Module"
        )
```

---

# Registering Modules

Add the import to:

```text
cli/scan.py
```

Example:

```python
from modules.my_module import (
    MyModule
)
```

Register:

```python
MODULE_MAP = {

    "my_module":
    MyModule
}
```

---

# Module Dependencies

Modules can depend on other modules.

Example:

```python
dependencies = [
    "httpx"
]
```

AutoRec automatically resolves execution order.

---

# Output Structure

Each scan generates a workspace:

```text
output/
└── example.com_timestamp/
```

Typical structure:

```text
subdomains/
dns/
http/
urls/
js/
screenshots/
priority/
```

Store module output inside its own directory whenever possible.

---

# Wordlists

Custom wordlists can be stored in:

```text
wordlists/
```

Example:

```text
wordlists/custom.txt
```

These files are intentionally excluded from Git tracking.

---

# Dashboard

Dashboard files are located in:

```text
dashboard/
```

Templates:

```text
dashboard/templates/
```

You may modify:

* Layout
* Navigation
* Tables
* Statistics
* Search pages

to suit your workflow.

---

# Reports

HTML report template:

```text
templates/report.html
```

Report generator:

```text
reporting/html_report.py
```

You can customize:

* Executive Summary
* Findings
* Screenshots
* Priority Views
* Branding

---

# Database

Schema:

```text
database/schema.sql
```

Repository Layer:

```text
database/repository.py
```

New modules should use the repository whenever possible rather than writing directly to reports.

---

# Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

---

# Recommended Custom Modules

Examples of useful extensions:

* ASN Enumeration
* Cloud Asset Discovery
* GitHub Recon
* Technology Correlation
* Asset Risk Scoring
* Historical Diffing
* Notification Integrations
* Custom Nuclei Workflows

---

# Best Practices

* Keep modules focused on a single task.
* Use repository storage for findings.
* Avoid hardcoded paths.
* Store outputs in module-specific folders.
* Update profiles when adding modules.
* Document new features in README and ROADMAP.

---

Happy hacking and happy building.
