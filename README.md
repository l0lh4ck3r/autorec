# AutoRec

AutoRec is a modular reconnaissance automation framework designed for bug bounty hunting, attack surface mapping, and continuous reconnaissance.

It combines subdomain discovery, DNS resolution, HTTP probing, URL collection, screenshotting, asset correlation, reporting, Docker deployment, and a web dashboard into a single workflow.

---

## Features

### Recon Pipeline

* Subdomain Discovery (Subfinder)
* DNS Resolution (DNSX)
* HTTP Enumeration (HTTPX)
* URL Collection (GAU)
* Historical URL Collection (WaybackURLs)
* Screenshot Capture (GoWitness)

### Asset Inventory

Automatically stores:

* Subdomains
* Resolved Hosts
* HTTP Services
* Technologies
* URLs
* Screenshots

### Correlation Engine

Detects interesting assets and URLs using scoring rules.

Examples:

* Admin Panels
* Login Pages
* API Endpoints
* Sensitive Paths
* Interesting Technologies

### Database

SQLite-backed storage for:

* Scans
* Assets
* Findings
* Technologies
* URLs
* Screenshots

### Reporting

* HTML Reports
* Asset Inventory
* Findings Summary

### Dashboard

Web dashboard with:

* Overview Statistics
* Asset Inventory
* Findings Viewer
* Screenshot Gallery

### Docker Support

Run AutoRec inside Docker with minimal setup.

---

# Installation

## Requirements

### Python

* Python 3.12+

### Go

Required tools:

* Subfinder
* DNSX
* HTTPX
* GAU
* WaybackURLs

---

## Clone Repository

```bash
git clone https://github.com/l0lh4ck3r/autorec.git

cd autorec
```

---

## Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Go Tools

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest

go install github.com/projectdiscovery/httpx/cmd/httpx@latest

go install github.com/lc/gau/v2/cmd/gau@latest

go install github.com/tomnomnom/waybackurls@latest
```

---

# Quick Start

## Full Scan

```bash
python autorec.py scan example.com --profile full
```

Output:

```text
output/
└── example.com_YYYYMMDD_HHMMSS/
    ├── subdomains/
    ├── dns/
    ├── http/
    ├── urls/
    ├── screenshots/
    └── scan.db
```

---

## Dashboard

Start dashboard:

```bash
python dashboard/app.py
```

Open:

```text
http://localhost:5000
```

Available pages:

```text
/
 /assets
 /findings
 /screenshots
```

---

# Docker

Build image:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

---

# Database Schema

Main tables:

```text
scans
asset_inventory
findings
technologies
url_inventory
screenshots
scan_state
```

---

# Project Structure

```text
autorec/
├── autorec.py
├── core/
├── database/
├── modules/
├── correlation/
├── reporting/
├── dashboard/
├── output/
├── logs/
├── wordlists/
└── latest.db
```

---

# Current Modules

| Module      | Purpose                  |
| ----------- | ------------------------ |
| Subfinder   | Subdomain Discovery      |
| DNSX        | DNS Resolution           |
| HTTPX       | HTTP Enumeration         |
| GAU         | URL Collection           |
| WaybackURLs | Historical URL Discovery |
| GoWitness   | Screenshot Collection    |

---

# Roadmap

## Completed

* Recon Pipeline
* SQLite Database
* Correlation Engine
* HTML Reports
* Docker Support
* Dashboard
* Screenshot Gallery

## Planned

### Phase 13B.2

* URL Inventory Page
* Technology Inventory Page
* Scan History Page

### Phase 14

* Nuclei Integration

### Phase 15

* JavaScript Analysis

### Phase 16

* Notifications

  * Discord
  * Slack
  * Telegram

### Phase 17

* Live Dashboard
* WebSockets
* Real-time Scan Progress

---

# Example Dashboard

Features currently available:

* Dashboard Overview
* Asset Inventory
* Findings Viewer
* Screenshot Gallery

---

# Disclaimer

This tool is intended for authorized security testing, bug bounty programs, and defensive security assessments only.

Users are responsible for complying with all applicable laws, policies, and program rules.

---

# Author

<mark>l0lh4ck3r</mark>

GitHub:
https://github.com/l0lh4ck3r