# AutoRec

AutoRec is a modular reconnaissance automation framework for attack surface discovery, bug bounty hunting, and continuous reconnaissance.

It combines asset discovery, URL collection, technology fingerprinting, screenshotting, correlation, reporting, Docker deployment, and a dynamic web dashboard into a unified workflow.

---

## Features

### Recon Pipeline

* Subfinder
* DNSX
* HTTPX
* GAU
* WaybackURLs
* GoWitness

### Asset Inventory

Automatically discovers and stores:

* Subdomains
* Resolved Hosts
* HTTP Services
* URLs
* Technologies
* Screenshots

### Correlation Engine

Automatically scores and identifies interesting findings:

* Admin Panels
* Login Pages
* APIs
* Sensitive Paths
* Interesting Technologies

### Dashboard

Available pages:

* Dashboard Overview
* Asset Inventory
* URL Inventory
* Technology Inventory
* Findings Viewer
* Screenshot Gallery
* Scan History

### Reporting

* HTML Reports
* Findings Summary
* Asset Inventory Reports

### Deployment

* Native Python
* Docker
* Docker Compose

---

## Installation

### Requirements

* Python 3.12+
* Go 1.22+
* SQLite3
* Docker (optional)

### Clone Repository

```bash
git clone https://github.com/l0lh4ck3r/autorec.git

cd autorec
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Recon Tools

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/lc/gau/v2/cmd/gau@latest
go install github.com/tomnomnom/waybackurls@latest
```

---

## Usage

### Full Scan

```bash
python autorec.py scan example.com --profile full
```

### Launch Dashboard

```bash
python dashboard/app.py
```

Browse:

```text
http://localhost:5000
```

Available routes:

```text
/
/assets
/urls
/technologies
/findings
/screenshots
/scans
```

---

## Database

Primary tables:

```text
scans
asset_inventory
url_inventory
technologies
findings
screenshots
scan_state
```

---

## Docker

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

---

## Roadmap

### Completed

* Recon Pipeline
* SQLite Storage
* Correlation Engine
* HTML Reports
* Docker Support
* Dashboard Core
* Asset Inventory
* URL Inventory
* Technology Inventory
* Findings Viewer
* Screenshot Gallery
* Scan History

### Next

* Search
* Pagination
* Filtering
* Nuclei Integration
* JavaScript Analysis
* Notifications
* Live Dashboard

---

## Disclaimer

This project is intended for authorized security testing and defensive security assessments only.

Always obtain permission before testing any target systems.

---

## Author

l0lh4ck3r

GitHub:
https://github.com/l0lh4ck3r
