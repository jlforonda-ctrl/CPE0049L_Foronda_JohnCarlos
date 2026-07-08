## Task 1: AI-Driven Architectural Migration

**Prompt Used:**
"Here is the legacy code. Generate a C4 Level 2 Container diagram in Mermaid.js, identify three code smells, and implement the Factory and Strategy patterns for the data stream [78, 82, 91, 65, 40, 99, 88] using Encryption Key: 0x4F and Compression Factor: 0.85."

**AI-Generated Block:**
Generated a Mermaid.js C4 Container diagram, listed three code smells based on the legacy monolith, and provided Python code for `factory.py` and `strategy.py`.

**Manual Verification/Correction Steps:**
Reviewed the Mermaid syntax to ensure it accurately maps the legacy system's structure. Checked `factory.py` and `strategy.py` to confirm no hallucinated library methods were called. Verified that the Strategy Pattern accurately processes the required dataset using the exact Encryption Key (0x4F) and Compression Factor (0.85) without hallucinated syntax.
## Task 2: Supply-Chain & Security Integrity

**Prompt Used:**
"Provide the Python implementation for JWT authentication, a mock security audit for SECURITY.md, and an explanation of the JWT cryptographic handshake for my migration report."

**AI-Generated Block:**
Generated `src/auth.py` using PyJWT, drafted `SECURITY.md` detailing dependency pinning and mock vulnerabilities, and wrote the JWT handshake explanation.

**Manual Verification/Correction Steps:**
Reviewed the PyJWT implementation to ensure the `HS256` algorithm is used correctly for encoding and decoding. Verified that `SECURITY.md` accurately flags the hardcoded secret key as a mock vulnerability. Confirmed the handshake explanation correctly describes the HMAC SHA-256 process.
## Task 3: CI/CD Pipeline & Automated Quality Gates

**Prompt Used:**
"Generate the GitHub Actions workflow file to include linting, security, and testing stages, ensuring it fails if coverage falls below 85%."

**AI-Generated Block:**
Generated the YAML configuration for `.github/workflows/main.yml` containing steps for flake8, bandit, and pytest with a `--cov-fail-under=85` flag.

**Manual Verification/Correction Steps:**
Reviewed the YAML syntax to ensure the quality gates were ordered correctly and verified that the `pytest` command explicitly includes the strict coverage constraint required by the exam parameters.