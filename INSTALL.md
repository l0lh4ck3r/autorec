# Installation Guide

## Parrot OS

Update system:

```bash
sudo apt update
sudo apt upgrade -y
```

Install Python:

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Install Go:

```bash
sudo apt install golang-go -y
```

Install Recon Tools:

```bash
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest

go install github.com/projectdiscovery/httpx/cmd/httpx@latest

go install github.com/lc/gau/v2/cmd/gau@latest

go install github.com/tomnomnom/waybackurls@latest

go install github.com/sensepost/gowitness@latest
```

Add Go binaries to PATH:

```bash
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc

source ~/.bashrc
```

Clone AutoRec:

```bash
git clone <repository>

cd autorec
```

Create Virtual Environment:

```bash
python -m venv venv

source venv/bin/activate
```

Install Python Requirements:

```bash
pip install -r requirements.txt
```

Verify:

```bash
python autorec.py doctor
```

## Kali Linux

Same steps as Parrot OS.

## Ubuntu

Same steps as Parrot OS.
