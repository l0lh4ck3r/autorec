# AutoRec

AutoRec is an automated reconnaissance framework that combines asset discovery, URL collection, technology fingerprinting, screenshot capture, correlation, and reporting into a single workflow.

## Features

* Subdomain Discovery
* DNS Resolution
* HTTP Probing
* URL Collection
* Technology Detection
* Screenshot Collection
* SQLite Storage
* Correlation Engine
* HTML Dashboard
* Asset Inventory
* Search
* Statistics

## Architecture

Target
↓
Subfinder
↓
DNSX
↓
HTTPX
↓
GAU / Waybackurls
↓
Gowitness
↓
SQLite
↓
Dashboard

## Installation

```bash
git clone <repository>

cd autorec

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Dependencies

The following tools must be installed and available in PATH:

* subfinder
* dnsx
* httpx
* gau
* waybackurls
* gowitness

## Verify Installation

```bash
python autorec.py doctor
```

## Usage

### Quick Scan

```bash
python autorec.py scan example.com
```

### Full Scan

```bash
python autorec.py scan example.com --profile full
```

### Statistics

```bash
python autorec.py stats
```

### Search

```bash
python autorec.py search admin
```

### Rebuild Report

```bash
python autorec.py rebuild-report
```

### Dashboard

```bash
python autorec.py dashboard
```

## Output Structure

output/

└── target_timestamp/

├── dns/

├── http/

├── urls/

├── screenshots/

└── report.html

## Database

Database file:

latest.db

Tables:

* scans
* hosts
* urls
* asset_inventory
* url_inventory
* technologies
* screenshots
* findings

## Current Status

Version: 1.0 Release Candidate

Implemented:

* Scanner Engine
* Dashboard
* Screenshots
* Database
* Correlation Engine
* Search
* Statistics

Planned:

* Docker Support
* FastAPI Dashboard
* Real-Time Logs
* Enhanced Correlation Rules
