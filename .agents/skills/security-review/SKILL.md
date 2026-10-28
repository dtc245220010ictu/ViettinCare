---
name: security-review
description: Audit software architecture, implementation, and AI integrations for cybersecurity vulnerabilities and compliance with privacy rules.
---
# Security Review Skill
## Objective
Conduct security assessments covering OWASP Top 10 web vulnerabilities, customer PII exposure, AI prompt injection, and secrets management.

## Inputs
Read:
- Source code in repository
- Configuration files (`.env.example`, `requirements.txt`)
- Architecture document `docs/architecture.md`

## Process
Checklist:
1. SQL Injection (Parameterized queries, ORM usage)
2. Cross-Site Scripting (XSS - template auto-escaping, innerHTML precautions)
3. Cross-Site Request Forgery (CSRF tokens)
4. Authentication (Password hashing via bcrypt, session management, secure cookies)
5. Authorization (Role-based access control checking on each route)
6. Secrets Management (No hardcoded API keys/passwords in source control)
7. Input Validation & Sanitization (Strict schema validation on ticket creation/commenting)
8. AI Specific Risks:
   - Prompt Injection & Jailbreaking mitigations
   - PII Sanitization (Customer phone numbers, emails, passwords stripped/masked before sending to external LLM)
   - Hallucination safeguard: Explicit policy forbidding AI from making unilateral promises (refunds, warranty overrides)
9. Dependency Vulnerabilities (`safety` or `pip-audit`)
10. Information Leakage (No stack traces returned to client endpoints)

## Outputs
- `docs/security-review.md`
