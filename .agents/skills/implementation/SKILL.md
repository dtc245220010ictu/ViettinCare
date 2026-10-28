---
name: implementation
description: Implement software components in Python (Flask/FastAPI) following architecture, database design, and clean code principles.
---
# Implementation Skill
## Objective
Implement modular, maintainable, secure application code strictly following approved requirements, architecture specifications, and database schema.

## Inputs
Read:
- docs/requirements.md
- docs/architecture.md
- docs/database-design.md

## Process
1. Read Specification
2. Understand Architecture & Component Boundaries
3. Understand Database Models & Migrations
4. Implement:
   - Database connection & DAO / Repository
   - Authentication & Role middleware
   - Customer Management CRUD
   - Ticket Management CRUD & status transition
   - Filter, search & statistics queries
   - AI service integration with strict PII masking & human approval workflow
   - Front-end views and templates
5. Run Linter (Flake8 / Pylint / Black)
6. Run Automated Tests
7. Review Git Diff & ensure no scope creep

## Rules
- Do not modify approved requirements or architecture.
- Do not hardcode secrets or API keys (use `.env`).
- Never allow external AI direct access to database queries.
- Stop and ask when specifications are ambiguous instead of assuming.

## Outputs
- Source code in `models/`, `routes/`, `services/`, `templates/`, `static/`, `app.py`

