---
name: code-review
description: Perform structured, unbiased code review focusing on correctness, requirements adherence, architecture boundaries, maintainability, and error handling.
---
# Code Review Skill
## Objective
Evaluate code quality, enforce architectural guidelines, detect code smells, unhandled exceptions, and logic bugs prior to merging.

## Inputs
Read:
- docs/requirements.md
- docs/architecture.md
- Project source code in `app.py`, `models/`, `routes/`, `services/`

## Process
1. Check Correctness against Functional Requirements
2. Check Architecture & Layer Separation Compliance
3. Check Code Quality & Maintainability (PEP 8, DRY, SOLID)
4. Check Duplication & Complexity
5. Check Error Handling & Logging (safe exception catching)
6. Check Database Access Patterns (avoid N+1 queries, use parameterized statements)
7. Check Test Quality & Coverage
8. Classify Findings into:
   - CRITICAL (must fix immediately before run)
   - HIGH (significant logic or stability risk)
   - MEDIUM (code smell, edge case unhandled)
   - LOW (styling, minor naming)

## Rules
- Do not modify source code directly during review.
- Focus on evidence-backed observations with file links and line numbers.

## Outputs
- `docs/code-review.md`

