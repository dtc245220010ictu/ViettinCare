---
name: architecture-design
description: Design software architecture from approved customer support requirements while preserving traceability and documenting architectural decisions.
---
# Architecture Design Skill
## Objective
Transform approved customer support requirements into a coherent, modular software architecture supporting both transactional ticket workflows and AI-assisted workflows (classification, summarization, response suggestion).

## Inputs
Read:
- docs/requirements.md
- docs/user-stories.md
- docs/acceptance-criteria.md
Only use approved requirements.

## Process
1. Identify architectural style (Layered MVC + Service-Oriented AI Pipeline).
2. Identify major components (Web UI, Controller/Routes, Ticket Service, Customer Service, Auth Service, AI Support Service, FAQ RAG Service, DB Repository).
3. Define responsibility of each component.
4. Define dependencies (Routes -> Services -> Models/Database & External AI API).
5. Define communication between components (Synchronous HTTP REST, JSON payloads).
6. Define data flow (User Request -> Controller -> Service -> Sanitization -> AI Engine -> Human Verification -> DB commit).
7. Identify external systems (Gemini LLM API, Email/Notification Gateway).
8. Identify security boundaries (Session Auth, RBAC middleware, PII Sanitizer before AI API call, Parameterized SQL queries).
9. Document architectural decisions (ADR format).
10. Check requirements-to-architecture traceability.

## Rules
- Do not implement source code.
- Do not modify approved requirements.
- Do not introduce unnecessary technologies.
- Every major architectural decision must have a rationale.
- Ensure external AI service cannot access the database directly.

## Outputs
Create:
- docs/architecture.md
- docs/architecture-decisions.md

## Verification
Verify that every major functional requirement is supported by at least one architectural component.
