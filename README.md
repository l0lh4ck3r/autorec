# AutoRec

AutoRec is a modular reconnaissance automation framework designed for bug bounty hunters, penetration testers, and security researchers.

It automates asset discovery, attack surface mapping, JavaScript analysis, vulnerability scanning, and reporting through a unified workflow.

## Features

### Discovery

* Subdomain Enumeration (Subfinder)
* DNS Resolution (DNSX)
* HTTP Enumeration (HTTPX)
* Historical URL Collection (GAU, WaybackURLs)

### Analysis

* JavaScript Discovery & Downloading
* Endpoint Extraction
* Secret Detection
* Authentication Mapping
* Interesting Endpoint Detection
* Screenshot Intelligence

### Validation

* GoWitness Screenshot Collection
* Nuclei Vulnerability Scanning

### Reporting

* SQLite Database Storage
* HTML Reports
* Correlation Engine
* Risk-Based Findings

## Quick Start

```bash
git clone https://github.com/<username>/autorec.git
cd autorec

pip install -r requirements.txt

python autorec.py scan example.com --profile full
```

## Profiles

### Quick

Fast asset discovery and validation.

### Full

Complete reconnaissance workflow including:

* URL Collection
* JavaScript Analysis
* Authentication Mapping
* Screenshot Intelligence
* Nuclei Scanning

## Current Status

* Asset Discovery ✅
* JavaScript Analysis ✅
* Authentication Mapping ✅
* Screenshot Intelligence ✅
* Vulnerability Discovery ✅
* HTML Reporting ✅

## Disclaimer

This tool is intended for authorized security testing and educational purposes only. Always obtain permission before scanning any target.
