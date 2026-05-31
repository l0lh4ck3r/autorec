# AutoRec Roadmap

## Current Version

**v0.4.0**

---

# Phase 1 - Foundation ✅

* Project Structure
* Module Framework
* Workspace Management
* Event Bus
* State Management
* Scan Profiles

Status: **Completed**

---

# Phase 2 - Database Layer ✅

* SQLite Integration
* Repository Pattern
* Scan Tracking
* Asset Storage
* Findings Storage

Status: **Completed**

---

# Phase 3 - Subdomain Discovery ✅

### Subfinder Integration

* Subdomain Enumeration
* Asset Inventory Population
* Database Integration

Status: **Completed**

---

# Phase 4 - DNS Resolution ✅

### DNSX Integration

* Host Resolution
* Resolved Host Tracking
* Asset Correlation

Status: **Completed**

---

# Phase 5 - HTTP Enumeration ✅

### HTTPX Integration

* Alive Host Detection
* Status Code Collection
* Title Detection
* Technology Detection

Status: **Completed**

---

# Phase 6 - URL Collection ✅

### GAU

* Historical URL Collection
* URL Inventory Storage

### WaybackURLs

* Archived URL Collection
* URL Inventory Storage

Status: **Completed**

---

# Phase 7 - Screenshot Collection ✅

### GoWitness Integration

* Screenshot Capture
* Screenshot Storage
* Screenshot Inventory

Status: **Completed**

---

# Phase 8 - Reporting ✅

### HTML Reports

* Scan Summary
* Asset Inventory
* Findings Summary

Status: **Completed**

---

# Phase 9 - Correlation Engine ✅

### Asset Correlation

* Interesting URL Detection
* Asset Scoring
* Severity Assignment

Status: **Completed**

---

# Phase 10 - Scan Persistence ✅

### Resume Capability

* Scan State Tracking
* Recovery Support

Status: **Completed**

---

# Phase 11 - Docker Support ✅

### Containerization

* Dockerfile
* Docker Compose
* Volume Mapping
* Portable Deployment

Status: **Completed**

---

# Phase 12 - Dashboard Core ✅

### Flask Dashboard

* Dashboard Homepage
* Statistics Overview
* Navigation System

Status: **Completed**

---

# Phase 13 - Dashboard Expansion 🚧

## Phase 13.1 ✅

### Dashboard Pages

* Asset Inventory
* Findings Viewer
* Screenshot Gallery

Status: **Completed**

---

## Phase 13.2

### Inventory Pages

* URL Inventory
* Technology Inventory
* Scan History

Status: **Planned**

---

## Phase 13.3

### Dashboard Improvements

* Search
* Filtering
* Pagination
* Sorting

Status: **Planned**

---

## Phase 13.4

### UI Improvements

* Bootstrap Styling
* Dark Mode
* Better Navigation
* Responsive Design

Status: **Planned**

---

# Phase 14 - Vulnerability Scanning

## Nuclei Integration

* Template Execution
* Vulnerability Storage
* Severity Tracking
* Dashboard Integration

Tables:

* nuclei_results

Status: **Planned**

---

# Phase 15 - JavaScript Analysis

### JavaScript Discovery

* JS File Inventory
* Endpoint Extraction
* Secret Detection
* API Discovery

Tables:

* javascript_files

Status: **Planned**

---

# Phase 16 - Parameter Mining

### URL Parameter Extraction

Examples:

* id=
* page=
* search=
* redirect=

Tables:

* parameters

Status: **Planned**

---

# Phase 17 - Continuous Recon

### Scan Comparison

* New Assets
* Removed Assets
* New Technologies
* New URLs

Features:

* Diff Reports
* Change Tracking

Status: **Planned**

---

# Phase 18 - Notifications

### Integrations

* Discord
* Slack
* Telegram

Triggers:

* New Asset
* High Severity Finding
* New Technology

Status: **Planned**

---

# Phase 19 - API Layer

### REST API

Endpoints:

* /api/assets
* /api/findings
* /api/urls
* /api/scans

Status: **Planned**

---

# Phase 20 - Real-Time Dashboard

### Live Monitoring

* WebSockets
* Live Logs
* Progress Tracking
* Real-Time Statistics

Status: **Planned**

---

# Future Ideas

### Cloud Support

* AWS Asset Discovery
* Azure Asset Discovery
* GCP Asset Discovery

### Additional Recon Sources

* Amass
* Assetfinder
* Katana
* Hakrawler

### Export Formats

* PDF
* JSON
* CSV

### Authentication

* User Accounts
* Role-Based Access

### Multi-Target Campaigns

* Organization Tracking
* Portfolio Monitoring

---

# Long-Term Vision

AutoRec aims to become a complete reconnaissance and attack-surface management platform capable of:

* Continuous Reconnaissance
* Asset Inventory Management
* Vulnerability Discovery
* Change Detection
* Reporting
* Team Collaboration
* Real-Time Monitoring

while remaining lightweight, modular, and easy to deploy.
