---
name: testing
description: Plan, design, and execute comprehensive automated tests (unit, integration, AI response validation) for the ticket management system.
---
# Testing Skill
## Objective
Verify functional correctness, boundary handling, authorization rules, and AI feature reliability using automated tests.

## Inputs
Read:
- docs/requirements.md
- docs/user-stories.md
- docs/acceptance-criteria.md

## Process
1. Analyze requirements & acceptance criteria
2. Derive Test Scenarios
3. Write Test Cases (Positive, Negative, Edge cases, Security boundary cases)
4. Implement Automated Tests (`tests/test_auth.py`, `tests/test_tickets.py`, `tests/test_ai_support.py`)
5. Execute Test Suite using `pytest`
6. Analyze Results & Defect Reporting
7. Measure Requirements Coverage

## Rules
- Do not modify tests merely to make them pass.
- Test both expected successes and forbidden operations (e.g. agent attempting admin action, unapproved AI response dispatch).
- Mock external AI API calls in unit tests to ensure deterministic execution.

## Outputs
- `docs/test-plan.md`
- `docs/test-report.md`
- Test files in `tests/`
