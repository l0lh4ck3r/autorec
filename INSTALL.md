# INSTALL.md

## Supported Platforms

### Tested

* Parrot OS 7.x
* Kali Linux
* Ubuntu 24.04+
* Debian 12+

---

## Prerequisites

### Python

```bash
python3 --version
```

Required:

```text
Python 3.12+
```

---

### Go

```bash
go version
```

Required:

```text
Go 1.22+
```

---

### Git

```bash
git --version
```

---

## Clone Repository

```bash
git clone https://github.com/l0lh4ck3r/autorec.git

cd autorec
```

---

## Python Environment

Create virtual environment:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Install Recon Tools

### Subfinder

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

### DNSX

```bash
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
```

### HTTPX

```bash
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
```

### GAU

```bash
go install github.com/lc/gau/v2/cmd/gau@latest
```

### WaybackURLs

```bash
go install github.com/tomnomnom/waybackurls@latest
```

### GoWitness

Install according to your operating system.

Verify:

```bash
gowitness version
```

---

## Verify Installation

Run:

```bash
subfinder -version

dnsx -version

~/go/bin/httpx --version

gau --version

waybackurls
```

---

## Important HTTPX Note

AutoRec uses the ProjectDiscovery HTTPX binary.

Some systems may also have the Python package:

```text
httpx
```

installed.

Verify:

```bash
which -a httpx
```

Expected:

```text
/home/<user>/go/bin/httpx
```

If multiple binaries exist, ensure the ProjectDiscovery version is used.

---

## Initialize Database

Run:

```bash
python autorec.py doctor
```

or:

```bash
python autorec.py scan example.com --profile full
```

This creates:

```text
latest.db
```

---

## Running AutoRec

### Full Scan

```bash
python autorec.py scan example.com --profile full
```

### Dashboard

```bash
python dashboard/app.py
```

Open:

```text
http://localhost:5000
```

---

## Docker Installation

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

---

## Troubleshooting

### HTTPX Error

Error:

```text
No such option '-l'
```

Cause:

Python HTTPX package is being used instead of ProjectDiscovery HTTPX.

Verify:

```bash
which -a httpx
```

Use:

```bash
~/go/bin/httpx --version
```

---

### Docker Error

Error:

```text
failed to connect to docker API
```

Check:

```bash
docker info
```

Ensure:

```bash
DOCKER_HOST
```

is not pointing to an invalid Podman socket.

Verify:

```bash
echo $DOCKER_HOST
```

Expected:

```text
(empty)
```

or:

```text
unix:///var/run/docker.sock
```

---

### Database Check

Verify:

```bash
sqlite3 latest.db
```

Useful queries:

```sql
SELECT COUNT(*) FROM asset_inventory;
SELECT COUNT(*) FROM url_inventory;
SELECT COUNT(*) FROM findings;
SELECT COUNT(*) FROM screenshots;
```