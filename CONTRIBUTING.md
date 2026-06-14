# Contributing to AutoRec

Thank you for your interest in contributing to AutoRec.

AutoRec is a modular reconnaissance automation framework focused on asset discovery, attack surface mapping, vulnerability validation, and reporting.

## Getting Started

### Fork the Repository

```bash
git clone https://github.com/<your-username>/autorec.git
cd autorec
```

### Create a Branch

```bash
git checkout -b feature/my-feature
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
python autorec.py doctor
```

---

## Development Guidelines

### Code Style

* Follow existing project structure.
* Keep modules focused on a single responsibility.
* Use descriptive variable and function names.
* Avoid hardcoded paths.
* Add comments only when necessary.

### Module Development

All reconnaissance modules should inherit from:

```python
ReconModule
```

Example:

```python
class MyModule(ReconModule):

    name = "my_module"

    dependencies = [
        "subfinder"
    ]

    async def run(self, context):
        pass
```

### Output Storage

Modules should store results using the Repository layer whenever possible.

Avoid writing results directly to reports.

---

## Testing

Before submitting a Pull Request:

```bash
python autorec.py doctor

python autorec.py scan example.com --profile quick
```

Verify:

* No crashes
* Report generation works
* Dashboard loads correctly
* Database entries are created

---

## Pull Requests

Please ensure:

* Code builds successfully
* Existing functionality is not broken
* Documentation is updated if needed
* New modules are added to:

  * `cli/scan.py`
  * `config/profiles.yaml`

### Commit Message Examples

```text
feat: add authentication mapping module

fix: improve JS endpoint extraction

docs: update installation guide

refactor: simplify repository queries
```

---

## Reporting Issues

When creating an issue, include:

* AutoRec version
* Operating system
* Python version
* Relevant logs
* Steps to reproduce

Example:

```text
Version: v1.0.0
OS: Parrot Security
Python: 3.12

Steps:
1. Run scan
2. Execute dashboard
3. Observe error
```

---

## Security Policy

Do not submit:

* Real credentials
* API keys
* Access tokens
* Sensitive customer data

All testing should be performed only on systems you own or are authorized to assess.

---

## Roadmap Areas

Contributions are especially welcome in:

* Correlation Engine
* Asset Risk Scoring
* Historical Diffing
* Dashboard Improvements
* Report Enhancements
* Performance Optimization
* Docker Improvements

---

## Code of Conduct

Be respectful and constructive.

The goal is to build a reliable and maintainable reconnaissance platform for the security community.

Happy hacking.
