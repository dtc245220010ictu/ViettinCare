---
name: documentation
description: Generate comprehensive, synchronized technical documentation reflecting current project implementation, architecture, APIs, and user guides.
---
# Documentation Skill
## Objective
Create clear, accurate, and up-to-date documentation for the customer support management system, ensuring consistency between codebase, database schema, and operational guides.

## Inputs
Read:
- `requirements.txt`, `app.py`
- `models/`, `routes/`, `services/`, `database/schema.sql`
- `docs/` artifacts

## Process
1. Inspect implemented features and endpoints.
2. Update `README.md` with setup, configuration, and running instructions.
3. Update `docs/api.md` with REST endpoints, request/response JSON schemas, and status codes.
4. Update `docs/architecture.md` with actual component interactions and sequence diagrams.
5. Update `docs/database-design.md` with actual ERD and schema dictionary.
6. Update `docs/deployment.md` with production deployment prerequisites and environment variables.
7. Update `docs/user-guide.md` with screenshots/workflows for Admin, Team Lead, and Support Agent.

## Rules
- Do not document fictional features not present in the code.
- Keep all setup commands tested and reproducible.
