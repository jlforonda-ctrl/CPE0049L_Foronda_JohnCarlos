# Security Audit & Supply Chain Integrity

## 1. Dependency Pinning
All third-party dependencies have been locked to exact versions in `requirements.txt` to prevent unauthorized upstream changes or supply-chain attacks.
* PyJWT
* pytest-cov
* flake8
* bandit

## 2. Mock Vulnerability Scanner Results
* **High Severity:** Hardcoded secret keys found in `auth.py`. 
    * *Remediation:* Move `SECRET_KEY` to an environment variable (`.env`) rather than committing it to version control.
* **Medium Severity:** `datetime.datetime.utcnow()` is deprecated in newer Python versions.
    * *Remediation:* Update to timezone-aware UTC objects.