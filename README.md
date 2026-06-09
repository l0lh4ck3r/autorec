# AutoRec

Automated Reconnaissance and Vulnerability Assessment Framework

## Overview

AutoRec is a modular reconnaissance and security assessment framework designed to automate bug bounty and penetration testing workflows. It combines subdomain enumeration, URL discovery, crawling, parameter extraction, vulnerability detection, technology fingerprinting, and risk scoring into a single pipeline.

The framework integrates multiple industry-standard tools and produces structured outputs suitable for manual validation and reporting.

---

## Features

## Current Capabilities

AutoRec currently provides an end-to-end reconnaissance and vulnerability discovery workflow.

### Reconnaissance

* Subdomain Enumeration (Subfinder)
* DNS Resolution (DNSX)
* HTTP Enumeration (HTTPX)
* Historical URL Collection (GAU)
* Historical URL Collection (WaybackURLs)
* Screenshot Collection (GoWitness)

### Asset Inventory

Automatically discovers and stores:

* Subdomains
* Resolved Hosts
* HTTP Services
* URLs
* Technologies
* Screenshots

### Technology Fingerprinting

Automatically detects:

* Web Servers
* CDNs
* Frameworks
* CMS Platforms
* Cloud Services
* Security Technologies

### Vulnerability Discovery

Nuclei integration provides:

* Vulnerability Scanning
* Severity Tracking
* Risk Scoring
* Findings Storage
* Dashboard Visibility

Supported severities:

* Critical
* High
* Medium
* Low
* Info

### JavaScript Analysis

Current capabilities:

* JavaScript URL Discovery
* JavaScript Inventory
* Endpoint Pattern Extraction

### Correlation Engine

Automatically identifies:

* Login Pages
* Administrative Interfaces
* API Endpoints
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

Dashboard features:

* Search
* Pagination
* Filtering
* Sorting
* Charts
* Risk Widgets
* Severity Analytics

### Reporting

* HTML Reports
* Findings Reports
* Asset Reports

### Deployment

Supported deployment methods:

* Native Python
* Docker
* Docker Compose

### Current Status

✅ Asset Discovery

✅ Technology Fingerprinting

✅ Historical URL Collection

✅ Screenshot Collection

✅ JavaScript Inventory

✅ Vulnerability Discovery

✅ Risk Scoring

✅ Dashboard Analytics

✅ Findings Management

✅ Recon Workflow Automation

### Recon Pipeline

* Subfinder
* DNSX
* HTTPX
* GAU
* WaybackURLs
* GoWitness
* Nuclei
* JavaScript Analysis

### Content Discovery

* URL collection from multiple sources
* Historical URL gathering
* Recursive crawling
* JavaScript file discovery

### Attack Surface Mapping

* Parameter extraction
* Sensitive file detection
* Endpoint classification
* Dynamic URL identification

### Vulnerability Detection

* Nuclei integration
* Misconfiguration detection
* Exposure checks
* Template-based scanning

### Reporting

* Risk scoring engine
* JSONL output
* Dashboard summaries
* Prioritized findings

* Dashboard Overview
* Asset Inventory
* URL Inventory
* Technology Inventory
* Findings Viewer
* Screenshot Gallery
* Scan History
* Search
* Pagination
* Filtering
* Sorting
* Charts
* Risk Widgets

## Current Workflow

```text
Target
   │
   ▼
Subdomain Enumeration
   │
   ▼
Live Host Validation
   │
   ▼
URL Collection
   │
   ▼
Crawler
   │
   ▼
Parameter Extraction
   │
   ▼
Nuclei Scanning
   │
   ▼
Risk Scoring
   │
   ▼
Final Report
```

---

## Project Structure

```text
autorec/
│
├── modules/
│   ├── subfinder_module.py
│   ├── httpx_module.py
│   ├── crawler_module.py
│   ├── nuclei_module.py
│   ├── param_module.py
│   └── ...
│
├── outputs/
│   ├── subdomains.txt
│   ├── live_hosts.txt
│   ├── urls.txt
│   ├── nuclei.jsonl
│   └── reports/
│
├── config/
│   ├── tools.yaml
│   └── settings.yaml
│
├── docs/
│
├── tests/
│
├── main.py
├── est_nuclei.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Requirements

### Operating System

* Linux (Recommended)
* Kali Linux
* Parrot OS
* Ubuntu

### Python

* Python 3.11+

### External Tools

Required tools:

* subfinder
* httpx
* katana
* waybackurls
* gau
* nuclei
* dnsx
* naabu (optional)

---

## Installation

Clone repository:

```bash
git clone https://github.com/<username>/autorec.git
cd autorec
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install ProjectDiscovery tools:

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/katana/cmd/katana@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

Update nuclei templates:

```bash
nuclei -update-templates
```

---

## Configuration

Example:

```bash
python autorec.py scan example.com --profile quick

python autorec.py scan example.com --profile full
```
Nuclei findings are automatically imported into SQLite and displayed in the dashboard.

---

## Usage

Run full workflow:

```bash
python main.py -d example.com
```

Run specific module:

```bash
python main.py --module nuclei
```

Run crawler only:

```bash
python main.py --module crawler
```

---

## Output Files

| File           | Description               |
| -------------- | ------------------------- |
| subdomains.txt | Enumerated subdomains     |
| live_hosts.txt | Active hosts              |
| urls.txt       | Collected URLs            |
| params.txt     | Parameters discovered     |
| nuclei.jsonl   | Raw nuclei findings       |
| report.json    | Final consolidated report |

---

## Risk Scoring

AutoRec assigns findings into:

* Critical
* High
* Medium
* Low
* Informational

Scoring considers:

* Vulnerability severity
* Endpoint sensitivity
* Exposure type
* Confidence level

---

## Roadmap

### Completed

* Subdomain enumeration
* URL discovery
* Crawler integration
* Nuclei integration
* Risk dashboard

### Planned

* JavaScript secret extraction
* Screenshot collection
* Authentication surface mapping
* AI-assisted prioritization
* Burp Suite export
* PDF reporting

---

## Disclaimer

This tool is intended for authorized security testing, bug bounty programs, and educational purposes only.

Always obtain permission before scanning any target.

---
