FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    unzip \
    golang-go \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/go/bin:${PATH}"

RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
RUN go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
RUN go install github.com/projectdiscovery/httpx/cmd/httpx@latest
RUN go install github.com/lc/gau/v2/cmd/gau@latest
RUN go install github.com/tomnomnom/waybackurls@latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "autorec.py", "--help"]